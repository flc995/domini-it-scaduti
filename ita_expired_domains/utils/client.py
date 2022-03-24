from httpx import AsyncClient
from typing import Type
from types import TracebackType
import asyncio


class Downloader:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.client: None | AsyncClient = None
    
    async def __aenter__(self):
        self.client = AsyncClient(base_url=self.base_url)
        return self

    async def __aexit__(self, exc_type: None | Type[BaseException], exc: None | BaseException, tb: None | TracebackType):
        await self.client.aclose()

    def compute_files_list(self, days_num: int):
        # TODO: Creare funzione per ritornare una lista di datetimes e portarla per creare i nomi dei files
        return []

    async def fetch_droptime_file(self, filename: str):
        return await self.client.get("/droptime/files/{filename}")

    async def fetch_droptime_files(self, days_num: int):
        filenames_list = self.compute_files_list(days_num)
        # Esegue multiple funzioni asincrone nello stesso momento
        files = await asyncio.gather(*(self.fetch_droptime_files(filename) for filename in filenames_list))



