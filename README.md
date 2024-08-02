# WhatsApp Chat Analyzer

This repository contains a WhatsApp Chat Analyzer built using Streamlit. The analyzer provides various insights and visualizations from WhatsApp chat data, including statistics, timelines, activity maps, emoji analysis, word clouds, and emotion scores.


## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Dependencies](#dependencies)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

The WhatsApp Chat Analyzer processes and visualizes WhatsApp chat data to provide insights into user activity, message frequency, most common words, and more. It also includes sentiment and emotion analysis based on emojis and message content.

## Overview

![image](https://github.com/user-attachments/assets/9338c459-1e41-4574-b09a-4c8bd532c4c2)
![image](https://github.com/user-attachments/assets/c0db02dc-8460-4743-aef9-fc6840bed232)
![image](https://github.com/user-attachments/assets/de49135f-207a-40f0-8f25-935ca883b986)
![image](https://github.com/user-attachments/assets/cecbedaa-0e0f-4403-8653-7261e1f04d21)
![image](https://github.com/user-attachments/assets/386f1c5b-043e-4f35-8cce-4425f12a9272)
![image](https://github.com/user-attachments/assets/f29f4f97-522c-44da-ac2a-fb6df5b642cc)
![image](https://github.com/user-attachments/assets/ca607052-7000-486d-81b8-d2a188d8ec04)
![image](https://github.com/user-attachments/assets/dd762c9a-1593-40ad-b2d0-ec43164dd359)
![image](https://github.com/user-attachments/assets/3d26abd3-1489-4f44-9973-b07dcfb1219f)

## Features

- **Top Statistics**: Total messages, words, media shared, and links shared.
- **Timelines**: Monthly and daily message timelines.
- **Activity Maps**: Most busy day and month, weekly activity heatmap.
- **Most Busy Users**: Identifies the most active users in the chat.
- **Emoji Analysis**: Frequency and distribution of emojis.
- **Word Cloud**: Visualization of the most common words.
- **Common Words**: List of the most frequently used words and emojis.
- **Emotion Scores**: Sentiment analysis of messages.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd whatsapp-chat-analyzer
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Upload your WhatsApp chat export file in `.txt` format using the file uploader in the sidebar.
3. Select the user to analyze or choose "overall" for overall chat analysis.
4. Click the "Show Analysis" button to generate the insights and visualizations.

## File Structure

Here's a comprehensive README.md file for your WhatsApp Chat Analysis project:

markdown
Copy code
# WhatsApp Chat Analyzer

This repository contains a WhatsApp Chat Analyzer built using Streamlit. The analyzer provides various insights and visualizations from WhatsApp chat data, including statistics, timelines, activity maps, emoji analysis, word clouds, and emotion scores.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Dependencies](#dependencies)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

The WhatsApp Chat Analyzer processes and visualizes WhatsApp chat data to provide insights into user activity, message frequency, most common words, and more. It also includes sentiment and emotion analysis based on emojis and message content.

## Features

- **Top Statistics**: Total messages, words, media shared, and links shared.
- **Timelines**: Monthly and daily message timelines.
- **Activity Maps**: Most busy day and month, weekly activity heatmap.
- **Most Busy Users**: Identifies the most active users in the chat.
- **Emoji Analysis**: Frequency and distribution of emojis.
- **Word Cloud**: Visualization of the most common words.
- **Common Words**: List of the most frequently used words and emojis.
- **Emotion Scores**: Sentiment analysis of messages.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd whatsapp-chat-analyzer
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Upload your WhatsApp chat export file in `.txt` format using the file uploader in the sidebar.
3. Select the user to analyze or choose "overall" for overall chat analysis.
4. Click the "Show Analysis" button to generate the insights and visualizations.

## File Structure

whatsapp-chat-analyzer/
├── app.py
├── functions.py
├── preprocessor.py
├── requirements.txt
└── README.md


- **app.py**: Main Streamlit app file.
- **functions.py**: Contains various helper functions for data analysis and visualization.
- **preprocessor.py**: Contains functions for preprocessing the chat data.
- **requirements.txt**: List of required Python libraries.

## Dependencies

- streamlit
- pandas
- matplotlib
- seaborn
- emoji
- urlextract
- wordcloud
- textblob

## Contributing 
   Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## License
  This project is licensed under the MIT License.
   
  This `README.md` file provides a clear overview of your project, including installation instructions, usage 
  guidelines, and a description of the file structure. Adjust the repository URL and any other specific details as 
  necessary.

   
