from flask import Flask, render_template, request
from collections import defaultdict

app = Flask(__name__)

# Partiju informācija
partijas_info = {
    'Jaunā VIENOTĪBA': {
        'uzsvari': 'Drošība, ekonomika, pārvaldība',
        'kopsavilkums': 'Jaunā VIENOTĪBA fokusējas uz efektīvu pārvaldību, drošību un ekonomisko izaugsmi.',
    },
    'Latvija Pirmajā Vietā': {
        'uzsvari': 'Tradīcijas, nacionālās intereses, uzņēmējdarbība',
        'kopsavilkums': 'Latvija Pirmajā Vietā aizstāv tradicionālās vērtības un koncentrējas uz uzņēmējdarbības attīstību.',
    },
    'Progresīvie': {
        'uzsvari': 'Videi draudzīga pilsēta, sociālā taisnīgums, līdzdalība',
        'kopsavilkums': 'Progresīvie strādā pie ilgtspējīgas attīstības, sabiedrības līdzdalības un sociālās taisnīguma.',
    },
}

# Jautājumi un atbildes
questions = [
    {
        'question': 'Kāda būtu Tava galvenā prioritāte Rīgas attīstībā?',
        'options': [
            ('Efektīva pārvaldība un droša vide', 'Jaunā VIENOTĪBA'),
            ('Nacionālo interešu aizsardzība un uzņēmējdarbība', 'Latvija Pirmajā Vietā'),
            ('Videi draudzīga pilsēta un vienlīdzība', 'Progresīvie')
        ]
    },
    {
        'question': 'Ko Tu sagaidi no Rīgas domes mēra?',
        'options': [
            ('Administratīvu pieredzi un pragmatisku pieeju', 'Jaunā VIENOTĪBA'),
            ('Spēcīgu līderi ar biznesa domāšanu', 'Latvija Pirmajā Vietā'),
            ('Sabiedriskuma un iedzīvotāju interešu aizstāvi', 'Progresīvie')
        ]
    },
    {
        'question': 'Kāds ir Tavs skatījums uz tradicionālajām vērtībām politikā?',
        'options': [
            ('Tām ir nozīme, bet lēmumiem jābūt balstītiem datos', 'Jaunā VIENOTĪBA'),
            ('Tradicionālā ģimene un konservatīvas vērtības ir prioritāte', 'Latvija Pirmajā Vietā'),
            ('Sabiedrībai jābūt atvērtai un iekļaujošai', 'Progresīvie')
        ]
    },
    {
        'question': 'Kas, Tavuprāt, visvairāk uzlabo rīdzinieku dzīves kvalitāti?',
        'options': [
            ('Efektīva pilsētas infrastruktūra un drošība', 'Jaunā VIENOTĪBA'),
            ('Ekonomiskie stimuli un investīciju piesaiste', 'Latvija Pirmajā Vietā'),
            ('Sabiedriskais transports, zaļās zonas un pieejami pakalpojumi', 'Progresīvie')
        ]
    }
]

# Route mājaslapai, kur ir jautājumi
@app.route('/')
def index():
    return render_template('index.html', questions=questions)

# Route rezultātu parādīšanai
@app.route('/results', methods=['POST'])
def results():
    answers = request.form
    party_scores = defaultdict(int)

    # Aprēķinām punktus
    for question in questions:
        selected_answer = answers.get(question['question'])
        if selected_answer:
            party_scores[selected_answer] += 1

    # Kopējais punktu skaits
    total_questions = len(questions)
    results = {}
    for party, score in party_scores.items():
        percentage = (score / total_questions) * 100
        results[party] = {
            'percentage': round(percentage, 2),
            'info': partijas_info[party]['kopsavilkums']
        }

    return render_template('results.html', results=results, partijas_info=partijas_info)

if __name__ == '__main__':
    app.run(debug=True)
