import urllib.request as urllib2
import datetime

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
                print("Parsing: ", url_to_fetch)
                domains = self.parse_url(url=url_to_fetch)
                domain_list.extend(domains)
        print('Domains:', *sorted(domain_list), sep='\n')

print("Benvenuto nel tool di ricerca di domini (.it) appena scaduti. Inserire numero di giorni da cercare (es: ultimi 4 giorni) e numero di caratteri del dominio (almeno 5)")
days = input("Inserire il numero di giorni che si vuole cercare (max 8): ")
length = input("Inserire la lunghezza del dominio desiderato (consigliabile maggiore di 5): ")
my_parser = NICParser(days=int(days), domain_length=int(length))
my_domains = my_parser.parse_domains()
