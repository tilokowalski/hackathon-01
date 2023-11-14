# Topic Interest and Skill Level Visualization

## Description
This script (plot.py) generates bar charts for various topics based on participants' interest and skill levels. Each chart represents a topic and shows the interest and skill levels of different participants as well as the average values across all participants. The values are presented as percentages.

## Usage
1. Ensure that data.json is in the same directory as plot.py. This JSON file should contain the data about topics and participants in the prescribed format.
2. Run the script using a Python interpreter. For example:
   ```bash
   python plot.py
   ```
3. The script will read data from data.json and generate bar charts, saving them into [topics/graphics/](topics/graphics/).

## Output
- Each topic will have a corresponding bar chart saved as a PNG image in the graphics directory.
- The charts display interest and skill levels for each participant and the average across participants.
- Values are indicated on the bars, rounded to the nearest whole number.

## Requirements
- Python 3.x
- Matplotlib library (Install using pip install matplotlib)

Note: This script is a simple visualization tool and does not perform any advanced data processing or statistical analysis.