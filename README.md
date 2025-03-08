# Market Clock

Market Clock is a minimalistic command-line clock that tracks the current trading status of multiple stock exchanges worldwide. It uses the released trading holidays to determine whether the markets are open or closed and counts down to the next trading event. 

![](/screenshots/screen.png)

## Features

- Displays trading status for major global stock exchanges including HKEX, LSE, NYSE and Nasdaq.
- Accounts for holidays and half trading days.
- Considers lunch breaks for exchanges with lunch hours.
- Real-time updates on when each market will open or close.

## Table of Contents
- [Installation](#installation)
- [Supported Markets](#supported-markets)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

`uv` is needed. Install it if you haven't:

```bash
pip install uv
```

To use Market Clock, install it as a uv tool:

```bash
uv tool install market-clock
market-clock
```

or you can invoke it without installing:

```bash
uvx market-clock
```

To exit the application, simply press `Ctrl + C`.

## Usage

Market Clock supports several command line arguments to customize its behavior:

`--markets`: Specify which market(s) to display. For example, to show only NYSE and Nasdaq:

```bash
uvx market-clock --markets NYSE Nasdaq
```

  If no market is specified, it will display the status for all supported markets.

`--show-seconds`: Display seconds in the countdown timer. By default, seconds are hidden.

```bash
uvx market-clock --show-seconds
```

`--list-markets`: List all supported markets without starting the clock.

```bash
uvx market-clock --list-markets
```

This will display the trading status for the specified market. If no market is specified, it will display the status for all supported markets.

Market Clock currently supports the following exchanges:

| Exchange                      | Updated till| Source |
|-------------------------------|-------------|--------|
| NYSE (New York Stock Exchange)| 2027 EOY    | [NYSE](https://www.nyse.com/markets/hours-calendars)|
| Nasdaq| 2025 EOY    | [Nasdaq](https://www.nasdaq.com/market-activity/stock-market-holiday-schedule)|
| LSE (London Stock Exchange)   | 2026 EOY    | [LSE](https://www.londonstockexchange.com/equities-trading/business-days)|
| HKEX (Hong Kong Exchange)     | 2025 EOY    | [HKEX](https://www.hkex.com.hk/Services/Trading-hours-and-Severe-Weather-Arrangements/Trading-Hours/Securities-Market) |


## Contributing

Contributions are welcome! Please fork the repository and create a new branch for your feature or bug fix.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 
