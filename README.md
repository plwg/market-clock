# Market Clock

Market Clock is a command-line application that tracks the current trading status of multiple stock exchanges worldwide. It provides real-time updates on whether the markets are open or closed and counts down to the next trading event. 

## Features

- Displays trading status for major global stock exchanges including HKEX, LSE, and NYSE.
- Accounts for holidays and half trading days.
- Considers lunch breaks for exchanges with lunch hours.
- Real-time updates on when each market will open or close.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Supported Markets](#supported-markets)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use Market Clock, install it as a uv tool:

```bash
pip install uv
uv tool install market-clock
market-clock
```

or you can invoke it without installing

```bash
pip install uv
uvx market-clock
```

The terminal will display the trading status of supported markets, indicating if they are currently open or closed and counting down to the next close/open.

To exit the application, simply press `Ctrl + C`.

## Supported Markets

Market Clock currently supports the following exchanges:

- **HKEX (Hong Kong Exchange)**
    - Trading Days: Monday - Friday
    - Trading Hours: 09:30 - 16:00
    - Lunch Break: 12:00 - 13:00 (Yes)
  
- **LSE (London Stock Exchange)**
    - Trading Days: Monday - Friday
    - Trading Hours: 08:00 - 16:30
    - Lunch Break: None
  
- **NYSE (New York Stock Exchange)**
    - Trading Days: Monday - Friday
    - Trading Hours: 09:30 - 16:00
    - Lunch Break: None

## Contributing

Contributions are welcome! Please fork the repository and create a new branch for your feature or bug fix.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

--- 