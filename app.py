from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'Berlin', 'London', 'Rome'],
        'correct_answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune'],
        'correct_answer': 'Mars'
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/results', methods=['POST'])
def results():
    score = 0
    answers = request.form
    for q in questions:
        selected = answers.get(q['question'])
        if selected == q['correct_answer']:
            score += 1
    return render_template('results.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run()
