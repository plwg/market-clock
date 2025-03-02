# Market Clock

[Github](https://github.com/plwg/market-clock)

Market Clock is a minimalistic command-line application that tracks the current trading status of multiple stock exchanges worldwide. It uses the released trading holidays to determine whether the markets are open or closed and counts down to the next trading event. 

![](/screenshots/screen.png)

## Features

- Displays trading status for major global stock exchanges including HKEX, LSE, and NYSE.
- Accounts for holidays and half trading days.
- Considers lunch breaks for exchanges with lunch hours.
- Real-time updates on when each market will open or close.

## Table of Contents
- [Installation](#installation)
- [Supported Markets](#supported-markets)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use Market Clock, install it as a uv tool:

```bash
pip install uv
uv tool install market-clock
market-clock
```

or you can invoke it without installing:

```bash
pip install uv
uvx market-clock
```

To exit the application, simply press `Ctrl + C`.

## Supported Markets

Market Clock currently supports the following exchanges:

| Exchange                      | Updated till|
|-------------------------------|---------|
| NYSE (New York Stock Exchange) | 2027 EOY  |
| LSE (London Stock Exchange)   | 2026 EOY   |
| HKEX (Hong Kong Exchange)     | 2025 EOY   |


## Contributing

Contributions are welcome! Please fork the repository and create a new branch for your feature or bug fix.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 