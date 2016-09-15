from flask import *
from build import *

app = Flask(__name__)


# @app.before_request
# def before_request():
#     ConnectDatabase.db.connect()
#
#
# @app.after_request
# def after_request(response):
#     ConnectDatabase.db.close()
#     return response

@app.route('/')
def default_page():
    return render_template('index.html')


# add new data to the database
@app.route('/story', methods=['GET', 'POST'])
def add_story():
    if request.method == 'GET':
        return render_template('form.html', action="Create")
    elif request.method == 'POST':
        columns = ['title', 'story', 'criteria', 'value', 'estimation', 'status']
        data = [request.form[element] for element in columns]
        new_story = UserStory(
                    story_title=data[0],
                    user_story=data[1],
                    acceptance_criteria=data[2],
                    business_value=data[3],
                    estimation=data[4],
                    status=data[5])
        new_story.save()
        return redirect(url_for('default_page'))


@app.route('/list')
def list_story():
    story = UserStory.select()
    return render_template('list.html', user_stories=story, site='http://localhost:5000/delete', site2='http://localhost:5000/story')


@app.route('/story/<story_id>', methods=['GET'])
def show_stories(story_id):
    story = UserStory.get(UserStory.id == story_id)
    return render_template("form.html", user_story=story, action="Update")


@app.route('/story/<story_id>', methods=['POST'])
def edit_story(story_id):
    story = UserStory.update(story_title=request.form['title'],
                             user_story=request.form['story'],
                             acceptance_criteria=request.form['criteria'],
                             business_value=request.form['value'],
                             estimation=request.form['estimation'],
                             status=request.form['status']).\
                             where(UserStory.id == story_id)
    story.execute()
    return redirect(url_for('default_page'))


@app.route('/delete/<story_id>', methods=['GET'])
def delete_story(story_id):
    story = UserStory.get(UserStory.id == story_id)
    story.delete_instance()
    return redirect(url_for('list_story'))


app.run(debug=True)
