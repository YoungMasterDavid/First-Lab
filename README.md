# OSI Model Simulation in Python

## Description
This project simulates the **OSI Model** using Python. It implements all 7 layers and simulates data transmission. This does not connect to other devices because I didn't have any other device to try to connect to. Therefore, I only made this to open two terminals at the same time. First with the receiving and the second for the sending.

## Installation
1. Clone the repository:
git clone https://github.com/YoungMasterDavid/First-Lab.git

2. Create a virtual environment:
python -m venv venv source venv/bin/activate # For macOS/Linux venv\Scripts\activate # For Windows

## Execution
1. Open Terminal and type:
python -m osi_model.main server

2. Open another terminal and type:
python -m osi_model.main client

3. Output is at the first terminal