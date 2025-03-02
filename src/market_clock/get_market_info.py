import datetime
from datetime import date

import pytz


def get_lse_info():
    timezone = pytz.timezone("Europe/London")
    return (
        "LSE",
        timezone,
        datetime.time(8, 0),
        datetime.time(16, 30),
        datetime.time(12, 30),
        {
            date(2025, 4, 18),
            date(2025, 4, 21),
            date(2025, 5, 5),
            date(2025, 5, 26),
            date(2025, 8, 25),
            date(2025, 12, 25),
            date(2025, 12, 26),
            date(2026, 1, 1),
            date(2026, 4, 3),
            date(2026, 4, 6),
            date(2026, 5, 4),
            date(2026, 5, 25),
            date(2026, 8, 31),
            date(2026, 12, 25),
            date(2026, 12, 28),
            date(2027, 1, 1),
        },
        {
            date(2025, 12, 24),
            date(2025, 12, 31),
            date(2026, 12, 24),
            date(2026, 12, 31),
        },
    )


def get_nyse_info():
    timezone = pytz.timezone("America/New_York")
    return (
        "NYSE",
        timezone,
        datetime.time(9, 30),
        datetime.time(16, 0),
        datetime.time(13, 00),
        {
            date(2025, 1, 1),
            date(2025, 1, 20),
            date(2025, 2, 17),
            date(2025, 4, 18),
            date(2025, 5, 26),
            date(2025, 6, 19),
            date(2025, 7, 4),
            date(2025, 9, 1),
            date(2025, 11, 27),
            date(2025, 12, 25),
            date(2026, 1, 1),
            date(2026, 1, 19),
            date(2026, 2, 16),
            date(2026, 4, 3),
            date(2026, 5, 25),
            date(2026, 6, 19),
            date(2026, 7, 3),
            date(2026, 9, 7),
            date(2026, 11, 26),
            date(2026, 12, 25),
            date(2027, 1, 1),
            date(2027, 1, 18),
            date(2027, 2, 15),
            date(2027, 3, 26),
            date(2027, 5, 31),
            date(2027, 6, 18),
            date(2027, 7, 5),
            date(2027, 9, 6),
            date(2027, 11, 25),
            date(2027, 12, 24),
        },
        {
            date(2025, 7, 3),
            date(2025, 11, 28),
            date(2025, 12, 24),
            date(2026, 11, 27),
            date(2026, 12, 24),
            date(2027, 11, 26),
        },
    )