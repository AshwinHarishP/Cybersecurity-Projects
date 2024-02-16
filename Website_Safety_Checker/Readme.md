# Website Safety Checker

## Description

The Website Safety Checker is a Chrome extension that warns users about potentially unsafe websites by checking SSL validity and reputation using external APIs.

## Manifest

The `manifest.json` file contains the extension's metadata, permissions, and scripts configuration.

## Content Scripts

The `content.js` script contains functions for checking SSL validity and website reputation. It listens for navigation errors and reputation check requests.

## Popup UI

The `popup.html` and `popup.css` files define the user interface for the extension's popup. Users can input a website URL to check its safety.

## Background Script

The `background.js` script listens for messages from content scripts and performs actions based on the received requests, such as handling SSL issues or performing advanced reputation checks.

## Popup Script

The `popup.js` script handles user interactions in the popup UI, such as triggering safety checks when the user clicks the check button.

## Usage

To use the extension, install it in Chrome and click on the extension icon to open the popup. Enter a website URL and click "Check" to see if the website is safe.

## Credits

This project was created by [Ashwin Harish P].

## License

This project is licensed under the [MIT License](https://github.com/AshwinHarishP/Cybersecurity-Projects/blob/976cd6faa6e7f8b9de6fab7063a720a5f5151182/LICENSE).
