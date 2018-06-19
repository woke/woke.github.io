from flask import Flask, render_template, request, redirect, url_for
from card import read_data
from definitions import definitions

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
	return render_template('home.html')

@app.route("/topics/<topic>", methods=['GET'])
def topic(topic):
	#modfify topic to match format in definitions.py file
	topic_modified = topic.replace(" ", "_").lower()
	#check dictionary of topics to verify user trying to find a valid topic
	# Return 404 if user goes to an invalid page
	if topic_modified not in definitions:
		error = "Unfortunately, we couldn't find the page you searched for."
		return render_template('home.html', error=error), 404
	definition = definitions[topic_modified][0]
	definition_link = definitions[topic_modified][1]
	title_placement = topic.title()
	resources = read_data(topic_modified)
	return render_template('topic.html', topic=topic, title=title_placement,
	definition=definition ,resources=resources, definition_link=definition_link)

# Return 404 if user goes to an invalid page
@app.errorhandler(404)
def page_not_found(e):
	error = "We couldn't find the page you searched for."
	return render_template('home.html', error=error), 404


if __name__ == "__main__":
	app.run(debug=True)