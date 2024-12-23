# Health Buddy Chatbot

## Overview

Health Buddy is a simple, rule-based chatbot designed to provide health-related information and assistance. It uses basic Natural Language Processing (NLP) techniques to match user inputs with predefined responses. While it incorporates NLP for understanding user queries, it is not a fully AI-powered chatbot like those driven by advanced models (e.g., GPT-3). Instead, it is designed for straightforward interactions and can handle a limited range of predefined questions and answers.

## Features

- Responds to health-related queries using simple rule-based logic
- Predefined set of tags and responses for various user questions
- Handles basic queries such as health tips and general information

## Installation
### Clone the repository
```
git clone https://github.com/Aparnamol-KS/Chatbot.git
```
---
### Navigate to the project folder
```
cd Chatbot
```
---
### Install dependencies
```
pip install -r requirements.txt
```
---
### Train the Model
Run the `model_training.py` script to train the model and generate the necessary files.
```
python model_training.py
```
---
### Move Model Files
Once the model training is complete, you need to move the generated files to the model folder in the Flask application directory.

---
### Run the Flask Application
```
python app.py
```
The Flask app will start, and you can interact with the Health Buddy chatbot through your browser

---

## Limitations
+ The chatbot can only handle a limited set of predefined queries and does not learn from user interactions.
+ It may not be able to provide responses to complex or nuanced health-related questions.

## Future Improvements
+ Integrating more advanced AI techniques for better understanding of user queries
+ Expanding the set of questions and responses for a broader range of topics
