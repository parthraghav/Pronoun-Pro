# 🌈 PronounPro
## Chrome extension to neutralise the web!
[Learn more](/SUBMISSION.md)

## Instructions

### Download the repository
    git clone https://github.com/parthraghav/Pronoun-Pro PronounPro
    cd PronounPro

### (Server) Set up virtual environment
    cd server
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### (Server) Start the server
    python3 serve.py

### (Chrome) Install the extension
Upload the dist folder as unpacked extension to Chrome

### (Chrome) Development
    yarn install
    npm run watch
