# FarmAssist

## Introduction
FarmAssist is a Python application that suggests suitable crops to be planted based on user-provided parameters like area, budget, region, and geography. It utilizes the SQLite3 database for storing crop information and Qt Designer for designing the user interface.

## Features
- Easy-to-use graphical interface designed with Qt Designer.
- SQLite3 database integration to store and retrieve crop information.
- Efficient crop suggestion algorithm based on area, budget, region, and geography inputs.

## Requirements
- Python 3.x
- PyQt5 library
- SQLite3 database module

## Installation and Setup
1. Clone the repository: `git clone https://github.com/shubhamkothawade24/FarmAssist.git`
2. Install the required dependencies: `pip install PyQt5`
3. Ensure you have SQLite3 installed or install it from [SQLite Official Website](https://www.sqlite.org/download.html).

## How to Use
1. Run the `main.py` file to start the application.
2. Input the details like area, budget, region, and geography.
3. Click on the "Get Crop Suggestions" button to view the recommended crops.
4. Explore the suggested crops and make an informed decision on what to plant.

## Database Schema
The SQLite3 database contains the following tables:
- `crops`: Stores information about various crops, including their names, suitable regions, growth requirements, and more.

## Contribution Guidelines
We welcome contributions to improve FarmAssist and make it more useful for farmers and agriculture enthusiasts. If you'd like to contribute, please follow these steps:
1. Fork the repository and create a new branch for your feature or bug fix.
2. Implement your changes, following the project's coding style and best practices.
3. Submit a pull request with a clear description of your changes.

## License
FarmAssist is released under the [MIT License](https://opensource.org/licenses/MIT), which means you are free to use, modify, and distribute the code.

## Acknowledgments
We would like to thank the open-source community for their valuable contributions and support in making FarmAssist better.

## Contact
If you have any questions, feedback, or suggestions, please feel free to reach out to us at kothawadeshubham@kavruktechnologies.com

Happy farming with FarmAssist! 🚜🌱