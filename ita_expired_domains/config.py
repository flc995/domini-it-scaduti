import datetime


DEFAULT_BASE_URL = "https://www.nic.it"
DEFAULT_EXPIRING_HOURS: list[datetime.time] = [
    datetime.time(hour=9),
    datetime.time(hour=16)
]