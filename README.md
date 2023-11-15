# Topic Interest and Skill Level Evaluation for private mini Hackaton

## Description
The script [visualizer.py](visualizer.py) generates bar charts for various topics based on participants' interest and skill levels. Each chart represents a topic and shows the interest and skill levels of different participants as well as the average values across all participants. The values are presented as percentages.

## Usage
1. Ensure that [data.json](data.json) is in the same directory as [visualizer.py](visualizer.py). This JSON file should contain the data about topics and participants in the prescribed format.
2. Run the script using a Python interpreter. For example:

   ```bash
   python visualizer.py
   ```
3. The script will read data from [data.json](data.json) and generate bar charts, saving them into [topics/graphic/](topics/graphic/).

## Output
- Each topic will have a corresponding bar chart saved as a PNG image in the graphics directory.
- The charts display interest and skill levels for each participant and the average across participants.
- Values are indicated on the bars, rounded to the nearest whole number.

## Requirements
- Python 3.x
- Matplotlib library

   ```bash
   pip install matplotlib
   ```

Note: This script is a simple visualization tool and does not perform any advanced data processing or statistical analysis.

## Contribute

Your pull requests may include changes to the topic list and / or your personal interest and skill ratings which must include an updated version of the graphics.

- Make changes to the topic list directly in [topics/README.md](topics/README.md)
- Make changes to the ratings in [data.json](data.json)
   - Execute the script with to keep the visualization in sync to the data

   ```bash
   python visualizer.py
   ```