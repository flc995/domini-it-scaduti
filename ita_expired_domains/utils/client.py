from httpx import AsyncClient
from typing import Type
from types import TracebackType
import asyncio
import datetime
from ita_expired_domains.config import DEFAULT_BASE_URL, DEFAULT_EXPIRING_HOURS
import typer
class Downloader:
    def __init__(self, base_url: str, expiring_hours: list) -> None:
        self.base_url = base_url
        self.expiring_hours = expiring_hours
        self.client: None | AsyncClient = None
    
    async def __aenter__(self):
        self.client = AsyncClient(base_url=self.base_url)
        return self

    async def __aexit__(self, exc_type: None | Type[BaseException], exc: None | BaseException, tb: None | TracebackType):
        await self.client.aclose()

    def compute_files_list(self, days_num: int):
        # TODO: Creare funzione per ritornare una lista di datetimes e portarla per creare i nomi dei files
        last_days = []
        today = datetime.datetime.now()
        for x in range(int(days_num)):
            n_days_ago = today - datetime.timedelta(days=x)
            for x in self.expiring_hours:
                date = n_days_ago.strftime("%Y%m%d")
                date_with_hour = date + x
                last_days.append(date_with_hour)
        return last_days

    async def fetch_droptime_file(self, filename: str):
        url = f"{self.base_url}/droptime/files/{filename}.txt"
        typer.secho(f"Parsing: {url}", fg=typer.colors.BRIGHT_YELLOW)
        return await self.client.get(url)

    async def fetch_droptime_files(self, days_num: int):
        filenames_list = self.compute_files_list(days_num)
        files = await asyncio.gather(*(self.fetch_droptime_file(filename) for filename in filenames_list))
        return files

italian_register_client = Downloader(base_url=DEFAULT_BASE_URL, expiring_hours=DEFAULT_EXPIRING_HOURS)
