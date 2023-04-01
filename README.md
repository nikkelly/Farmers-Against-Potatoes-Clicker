# Farmers Against Potatoes Clicker

An automation tool for "Farmers Against Potatoes Idle", clicking on good potatoes for a seamless gaming experience.

## Features

- Auto-starts game
- Identifies & clicks good potatoes
- Countdown during breaks
- Sleeps before game restart

## Installation

1. Install Python 3.6+: [official website](https://www.python.org/downloads/)
2. Clone the repository: `git clone https://github.com/nikkelly/farmers-against-potatoes-clicker.git`
3. Change to project folder: `cd farmers-against-potatoes-clicker`
4. Install dependencies: `pip install -r requirements.txt`
5. Prepare images/960x540 folder with necessary images for game elements.

## Usage

Run the script: `python main.py`

The script auto-starts the game, clicks on good potatoes, and sleeps before restarting.

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b your-feature-branch`
3. Commit changes: `git commit -am 'Add a new feature'`
4. Push to branch: `git push origin your-feature-branch`
5. Create a new Pull Request

## License

Released under the [MIT License](https://opensource.org/licenses/MIT).

## Images

The images used by the script should be located in the `images/960x540` directory in the project folder. This directory should contain the following images:

- `start.png`: Image of the start button in the game.
- `goodPotato_1.png`: Image of a good potato to be clicked.
- `goodPotato_2.png`: Image of a second good potato to be clicked.
- `timetocount.png`: Image that appears when it is time to wait before restarting the game.
