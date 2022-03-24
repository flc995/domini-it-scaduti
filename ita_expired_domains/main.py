import typer
from ita_expired_domains.utils.client import italian_register_client
from ita_expired_domains.utils.misc import handle_nic_responses, filter_by_length, echo_urls
import asyncio

async def main():
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