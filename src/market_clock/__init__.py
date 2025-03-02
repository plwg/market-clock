import datetime
import time
from itertools import cycle

from blessed import Terminal

from market_clock.get_market_info import get_lse_info, get_nyse_info

def get_next_trading_day(start_date, holidays):
    next_day = start_date + datetime.timedelta(days=1)
    while True:
        if next_day.weekday() < 5 and next_day not in holidays:
            return next_day
        next_day += datetime.timedelta(days=1)


def format_timedelta(delta):
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_market_status(market_info):
    (
        market_name,
        timezone,
        start_time,
        end_time,
        half_day_end_time,
        holidays,
        half_days,
    ) = market_info

    local_time = datetime.datetime.now(timezone)
    current_time = local_time.time()
    current_date = local_time.date()

    if current_date > max(holidays | half_days):
        msg = f"{market_name} holiday list is not up-to-date."
        raise ValueError(msg)
    if holidays & half_days:
        msg = f"{market_name} has overlapping holidays/half-days"
        raise ValueError(msg)

    if current_date in holidays or local_time.weekday() >= 5:
        is_open = False
    elif current_date in half_days:
        is_open = start_time <= current_time <= half_day_end_time
    else:
        is_open = start_time <= current_time <= end_time

    if is_open:
        event_time = timezone.localize(
            datetime.datetime.combine(current_date, end_time)
        )
    elif (
        current_date.weekday() < 5
        and current_date not in holidays
        and current_time < start_time
    ):
        event_time = timezone.localize(
            datetime.datetime.combine(current_date, start_time)
        )
    else:
        next_day = get_next_trading_day(current_date, holidays)
        event_time = timezone.localize(datetime.datetime.combine(next_day, start_time))

    return is_open, event_time


def main():
    term = Terminal()
    spinner = cycle("🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦")
    lse_info = get_lse_info()
    nyse_info = get_nyse_info()

    with term.fullscreen(), term.hidden_cursor():
        try:
            while True:
                # Get market statuses
                is_lse_open, lse_event = get_market_status(lse_info)
                is_nyse_open, nyse_event = get_market_status(nyse_info)
                spinner_char = next(spinner)

                # Build display lines
                lse_line = (
                    f"{lse_info[0].rjust(6)} "
                    f"{'OPEN 🟢' if is_lse_open else 'CLOSED 🟠'} | "
                    f"{'Closes' if is_lse_open else 'Opens'} in "
                    f"{format_timedelta(lse_event - datetime.datetime.now(lse_info[1]))} "
                    f"{spinner_char}"
                )

                nyse_line = (
                    f"{nyse_info[0].rjust(6)} "
                    f"{'OPEN 🟢' if is_nyse_open else 'CLOSED 🟠'} | "
                    f"{'Closes' if is_nyse_open else 'Opens'} in "
                    f"{format_timedelta(nyse_event - datetime.datetime.now(nyse_info[1]))} "
                    f"{spinner_char}"
                )

                # Update display
                print(term.move(0, 0) + term.clear_eos + lse_line + "\n" + nyse_line)
                time.sleep(1)

        except KeyboardInterrupt:
            print(term.move_down(2) + "Countdown stopped.")


if __name__ == "__main__":
    main()
