# Chess AI using Alpha-Beta Pruning

## Overview
This Chess AI was built using the **Alpha-Beta Pruning** algorithm to optimize the Minimax decision-making process. The AI evaluates board positions and makes efficient moves by pruning unnecessary branches in the search tree, improving performance.

## Features
- Implements **Alpha-Beta Pruning** to enhance Minimax efficiency.
- Supports **basic chess rules** and move generation.
- Written in **Python** for ease of use and modification.
- Can play against a human player or another AI instance.

## Installation
Ensure you have Python installed, then clone the repository:

```bash
git clone https://github.com/nathanaelmbale/Chess-Ai.git
cd Chess-Ai
```

Install dependencies :

```bash
pip install -r requirements.txt
```

## Usage
Run the script to start the AI:

```bash
python ChessMain.py
```

Modify `depth` in the code to adjust the AI’s difficulty level.

## How It Works
The AI uses:
1. **Minimax Algorithm** – To determine the best possible move by evaluating future positions.
2. **Alpha-Beta Pruning** – To eliminate unnecessary calculations and speed up decision-making.
3. **Evaluation Function** – To assess board states based on material, position, and other heuristics.

## Future Improvements
- Implement a **GUI** using Pygame or Tkinter.
- Improve the evaluation function for better strategic play.
- Add support for **opening books** and **endgame databases**.
- Using a library like Tensorflow to train the Ai
  
## Contributions
Feel free to fork the repository and submit pull requests for improvements!

## License
This project is licensed under the MIT License.

---
Made with ❤️ by Nathanael Mbale.

