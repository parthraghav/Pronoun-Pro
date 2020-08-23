## Inspiration
COVID is being hailed as [the great equalizer](https://www.livemint.com/opinion/columns/opinion-corona-is-a-great-equalizer-the-final-choice-lies-with-us-11589824378372.html) in these tumultuous times, and yet it affects black gender minorities the most. Transphobia is disrupting more lives than ever, and yet somehow technology is going unused to solve problems that are faced by the LGBTQ community. Half of the world is on the internet and kids as young as [8 years old](https://www.csoonline.com/article/2225579/most-parents-allow-unsupervised-internet-access-to-children-at-age-8.html#:~:text=The%20answer%3A%20eight%20years%20old,like%20email%20or%20social%20networks.) are surfing it. I posit we need to create web tools for the next generation to leap out of the ignorance that often matures to take shape of transphobia. I posit if we erased the gender-binary from the web, our society will follow. 

## What it does
Pronoun Pro is a chrome extension that neutralizes gendered pronouns across all webpages on your browser. It is a sandbox for trans allies to practice using gender-neutral language on the web! My mission is to make web gender-free!

## How I built it
I began by making a text parser and tokenizers like nltk and spacy. I wrote a method to neutralize the text -- including the pronouns and the action verbs. I then also implemented an algorithm to maximize text readability in a long text. I then used Flask to serve the method through a POST API endpoint. At this point, I began working on the chrome extension. I read the documentation and quickly realized most of my work would be done using the content script. I wrote code to compile chunks of texts and then used jQuery to send the data in JSON form to the endpoint. On a 200 status code response, the gendered content is replaced with gender-neutral content!

## Challenges I ran into
Neutralizing coreferences not includes replacing the gendered pronoun with a gender-neutral counterpart but also changing the associated auxiliary and verb! After some work, I figured out a way to achieve that using the verb lemma and POS tags!

## Accomplishments that I'm proud of
I documented my code for the first half, and I finished the project just in time for the submission! I'm proud of that!

## What I learned
I learned a lot about the back-and-forth nature of NLP development! I quickly realized I should have been using Jupyter notebooks! I did learn about shipping quickly, at least in a hackathon setting. I was laser-focused on building and polishing the parts of the project that I would be demoing. My reading on Gender Neutral language to support my work strengthened my desire to finish the project in time!

## What's next for Pronoun-Pro
I have a dozen milestones for this open-sourced project, but the two most important ones are listed below:
1. Remove API dependency completely. I will be rewriting all my code to run on javascript. That would involve reinventing the wheel because javascript doesn't have a great NLP ecosystem just yet. 
2. Preserve paragraph styles. When the text is replaced, styles of children components are lost. I want to focus some time to solve this problem!
