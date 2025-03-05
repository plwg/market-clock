import datetime
from datetime import date
from zoneinfo import ZoneInfo

ALL_MARKET_INFO = {
    # https://www.hkex.com.hk/Services/Trading-hours-and-Severe-Weather-Arrangements/Trading-Hours/Securities-Market
    "HKEX": {
        "timezone": ZoneInfo("Asia/Hong_Kong"),
        "trading_weekdays": {0, 1, 2, 3, 4},
        "start_time": datetime.time(9, 30),
        "end_time": datetime.time(16, 0),
        "half_day_end_time": datetime.time(12, 00),
        "holidays": {
            date(2025, 1, 1),
            date(2025, 1, 29),
            date(2025, 1, 30),
            date(2025, 1, 31),
            date(2025, 4, 4),
            date(2025, 4, 18),
            date(2025, 4, 21),
            date(2025, 5, 1),
            date(2025, 5, 5),
            date(2025, 7, 1),
            date(2025, 10, 1),
            date(2025, 10, 7),
            date(2025, 10, 29),
            date(2025, 12, 25),
            date(2025, 12, 26),
        },
        "half_days": {
            date(2025, 1, 28),
            date(2025, 12, 24),
            date(2025, 12, 31),
        },
        "is_have_lunch_break": True,
        "lunch_break_start": datetime.time(12, 0),
        "lunch_break_end": datetime.time(13, 0),
    },
    # https://www.londonstockexchange.com/equities-trading/business-days
    "LSE": {
        "timezone": ZoneInfo("Europe/London"),
        "trading_weekdays": {0, 1, 2, 3, 4},
        "start_time": datetime.time(8, 0),
        "end_time": datetime.time(16, 30),
        "half_day_end_time": datetime.time(12, 30),
        "holidays": {
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
        "half_days": {
            date(2025, 12, 24),
            date(2025, 12, 31),
            date(2026, 12, 24),
            date(2026, 12, 31),
        },
        "is_have_lunch_break": False,
    },
    # https://www.nyse.com/markets/hours-calendars
    "NYSE": {
        "timezone": ZoneInfo("America/New_York"),
        "trading_weekdays": {0, 1, 2, 3, 4},
        "start_time": datetime.time(9, 30),
        "end_time": datetime.time(16, 0),
        "half_day_end_time": datetime.time(13, 00),
        "holidays": {
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
        "half_days": {
            date(2025, 7, 3),
            date(2025, 11, 28),
            date(2025, 12, 24),
            date(2026, 11, 27),
            date(2026, 12, 24),
            date(2027, 11, 26),
        },
        "is_have_lunch_break": False,
    },
    # https://www.nasdaq.com/market-activity/stock-market-holiday-schedule
    "Nasdaq": {
        "timezone": ZoneInfo("America/New_York"),
        "trading_weekdays": {0, 1, 2, 3, 4},
        "start_time": datetime.time(9, 30),
        "end_time": datetime.time(16, 0),
        "half_day_end_time": datetime.time(13, 00),
        "holidays": {
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
        },
        "half_days": {
            date(2025, 7, 3),
            date(2025, 11, 28),
            date(2025, 12, 24),
        },
        "is_have_lunch_break": False,
    },
}
