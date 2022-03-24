import urllib.request as urllib2
import datetime
import typer

class NICParser:

    base_url = "https://www.nic.it/droptime/files/"
    expiring_hours = ["09", "16"]

    def __init__(self, days, domain_length) -> None:
        self.days = days
        self.domain_length = domain_length

    def get_last_days(self):
        last_days = []
        today = datetime.datetime.now()
        for x in range(self.days):
            n_days_ago = today - datetime.timedelta(days=x)
            last_days.append(n_days_ago.strftime("%Y%m%d"))
        return last_days

    def get_full_url(self, date, hour):
        return f"{self.base_url}{date}{hour}.txt"

    def parse_url(self, url):
        data = urllib2.urlopen(url).read().decode('utf-8')
        url_list = data.split('\n')
        clean_list = list(filter(lambda x: x and len(x) <= self.domain_length, url_list))
        return clean_list

    def parse_domains(self):
        days_list = self.get_last_days()
        domain_list = []
        
        for x in days_list:
            for y in self.expiring_hours:
                url_to_fetch = self.get_full_url(date=x, hour=y)
                typer.secho(f"Parsing: {url_to_fetch}", fg=typer.colors.BRIGHT_YELLOW)
                domains = self.parse_url(url=url_to_fetch)
                domain_list.extend(domains)
        if len(domain_list) == 0:
            typer.secho("Nessun dominio trovato :( Riprovare aumentando i caratteri del dominio da cercare.", fg=typer.colors.BRIGHT_RED)
        else:
            for x in domain_list:
                domain = typer.style(x, fg=typer.colors.BRIGHT_GREEN)
                typer.echo(f"Available domain: {domain}")

