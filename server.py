from model import *
from flask import *

app = Flask(__name__)


@app.route('/story', methods=['GET', 'POST'])
def story():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        columns = ['title', 'story', 'criteria', 'value', 'estimation', 'status']
        data = [request.form[element] for element in columns]
        new_story = UserStory(
                    story_title=data[0], user_story=data[1], acceptance_criteria=data[2], business_value=data[3],
                    estimation=data[4], status=data[5])
        new_story.save()
        return redirect(url_for('story'))

app.run(debug=True)
