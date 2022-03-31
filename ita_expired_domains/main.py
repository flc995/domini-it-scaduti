import typer
from ita_expired_domains.utils.client import italian_register_client
from ita_expired_domains.utils.misc import handle_nic_responses, filter_by_length, echo_urls
import asyncio
import sys


async def main(args=sys.argv):
    """Gestiamo il comando con gli arguments (poetry run search 2 5) e senza (poetry run search)
    Nel secondo caso gestiamo gli input
    """
    args.pop(0)
    if len(args) == 2:
        days = args[0]
        length = args[1]
    else:
        typer.echo("Benvenuto nel tool di ricerca di domini (.it) appena scaduti. Inserire numero di giorni da cercare (es: ultimi 4 giorni) e numero di caratteri del dominio (almeno 5)")
        days = typer.prompt("Inserire numero di giorni da cercare (max. 8)")
        length = typer.prompt("Inserire i caratteri desiderati del dominio (consigliabile almeno 3)")
    
    async with italian_register_client as client:
        responses = await client.fetch_droptime_files(days_num=days)
    urls = handle_nic_responses(responses)
    filtered = filter_by_length(urls=urls, length=length)
    return echo_urls(filtered)

def start():
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())