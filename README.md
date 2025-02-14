# Text Summarization Web App

## Overview
This is a Flask-based web application for text summarization. The app takes user input, processes it using NLP techniques, and generates a concise summary. The UI is designed with an elegant and user-friendly theme.
## Live Server
https://smart-text-summarizer-1.onrender.com/
## Features
- **User-Friendly Interface**: A responsive and modern UI using HTML, CSS, and Google Fonts.
- **NLP-Powered Summarization**: Uses `spaCy` for text processing and summarization.
- **Real-Time Processing**: Summarizes text instantly upon submission.

## Technologies Used
- **Flask**: Web framework for Python.
- **spaCy**: NLP library for text processing.
- **HTML & CSS**: Styled UI with Google Fonts.

## Installation and Setup
### Prerequisites
Ensure you have Python 3.7+ installed on your system.

### Clone the Repository
```bash
git clone https://github.com/Dineshchowdaryjampala Smart_Text_Summarizer.git
 
```

### Install Dependencies
Create a virtual environment and install required dependencies:
```bash
pip install -r requirements.txt
```

### Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```

### Run the Application
```bash
python app.py
```
Open your browser and go to `http://127.0.0.1:5000/`.

## Deployment
For deploying on **Render, Heroku, or any cloud platform**, ensure:
- You have a `requirements.txt` file with dependencies.
- You specify `en_core_web_sm` in the build command (for Render):
  ```bash
  python -m spacy download en_core_web_sm
  ```
- Use a production-ready server like **Gunicorn**:
  ```bash
  gunicorn -w 4 -b 0.0.0.0:5000 app:app
  ```

## Author
Designed & Developed by **J DINESH CHOWDARY**  
Contact: [dineshwalker143@gmail.com](mailto:dineshwalker143@gmail.com)

## License
This project is licensed under the MIT License.

