import urllib.request as urllib2
import typer

def parse_txt_file(url, domain_length):
    data = urllib2.urlopen(url).read().decode('utf-8')
    url_list = data.split('\n')
    clean_list = list(filter(lambda x: x and len(x) <= domain_length, url_list))
    return clean_list

def handle_nic_responses(responses):
    """Convertiamo le response in testo e aggiungiamo gli url in un unica lista"""
    domains = []
    for r in responses:
        domains.extend(r.text.split('\n'))
    return [i for i in domains if i]

def echo_urls(urls):
    if len(urls) == 0:
            typer.secho("Nessun dominio trovato :( Riprovare aumentando i caratteri del dominio da cercare.", fg=typer.colors.BRIGHT_RED)
    for u in urls:
        domain = typer.style(u, fg=typer.colors.BRIGHT_GREEN)
        typer.echo(f"Available domain: {domain}")

def filter_by_length(urls, length):
    return sorted(list(filter(lambda x: x and len(x) <= int(length)+3, urls)))
