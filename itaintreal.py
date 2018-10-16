import random

from flask import (Flask, render_template)
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def index():
    (subject, actor, purpose) = get_data()
    return render_template('index.html', subject=subject, actor=actor, purpose=purpose)
    
def get_data():
    subject = get_random_line_from_file(Path('data/subject.txt'))
    actor = get_random_line_from_file(Path('data/actor.txt'))
    purpose = get_random_line_from_file(Path('data/purpose.txt'))

    return (subject, actor, purpose)

def get_random_line_from_file(path):
    lines = open(path, 'r').read().splitlines()
    return random.choice(lines)

if __name__ == '__main__':
    app.run(host='0.0.0.0')