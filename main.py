import typer
from lib.parser import NICParser

def main():
    typer.echo("Benvenuto nel tool di ricerca di domini (.it) appena scaduti. Inserire numero di giorni da cercare (es: ultimi 4 giorni) e numero di caratteri del dominio (almeno 5)")
    days = typer.prompt("Inserire numero di giorni da cercare (max. 8)")
    length = typer.prompt("Inserire i caratteri desiderati del dominio (consigliabile almeno 6)")
    my_parser = NICParser(days=int(days), domain_length=int(length))
    my_domains = my_parser.parse_domains()
    return my_domains

if __name__ == "__main__":
    typer.run(main)