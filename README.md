# 🌈 Pronoun Pro
## Chrome extension to neutralise the web!
![build status](https://api.cirrus-ci.com/github/flutter/flutter.svg "Build status")

Pronoun Pro is a chrome extension that neutralizes gendered pronouns across all webpages on your browser. It is a sandbox for trans allies to practice using gender-neutral language on the web! My mission is to make web gender-free!<br>
[Learn more](/SUBMISSION.md)

## Video Demo
https://www.youtube.com/watch?v=ZKkLR-Jmjwo

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

## Milestones
The project was made at the MHacks Hackathon. Following are some of the upcoming milestones:
- [ ] **Remove API dependency completely.** I will be rewriting all my code to run on javascript. That would involve reinventing the wheel because javascript doesn't have a great NLP ecosystem just yet.
- [ ] **Preserve paragraph styles.** When the text is replaced, styles of children components are lost. I want to focus some time to solve this problem!

## License
MIT
