import json
import matplotlib.pyplot as plt
import numpy as np
import os

# Function to read JSON data from a file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to add value annotations to each bar
def add_value_annotations(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{int(round(height))}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Function to create and save bar charts for each topic
def create_and_save_bar_charts(data, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define a softer color palette
    colors = plt.cm.Pastel1.colors

    for topic_info in data:
        topic = topic_info['topic']
        participants = topic_info['participants']

        names = [p['name'] for p in participants] + ['Average']
        interests = [p['interest'] * 100 for p in participants]
        skills = [p['skill'] * 100 for p in participants]

        # Calculate averages
        avg_interest = np.mean(interests)
        avg_skill = np.mean(skills)

        interests.append(avg_interest)
        skills.append(avg_skill)

        # Plotting
        x = np.arange(len(names))  # label locations
        width = 0.35  # width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, interests, width, label='Interest', color=colors[1])
        rects2 = ax.bar(x + width/2, skills, width, label='Skill', color=colors[2])

        # Add value annotations
        add_value_annotations(ax, rects1)
        add_value_annotations(ax, rects2)

        # Add zero value indicators
        for rect in rects1 + rects2:
            height = rect.get_height()
            if height == 0:
                rect.set_edgecolor(colors[0])
                rect.set_linewidth(2)

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Percentage')
        ax.set_title(f'Interest and Skill levels for {topic}')
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.set_ylim(0, 100)  # Set y-axis limit
        ax.legend()

        # Save the plot as an image
        plt.savefig(os.path.join(output_dir, f"{topic}.png"))
        plt.close()

# Main execution
if __name__ == "__main__":
    json_data = read_json_file('rating.json')
    create_and_save_bar_charts(json_data, 'images')
