from flask import *
import os


app = Flask(__name__)

@app.route('/api_filesIn')
def api_get_files():
	return jsonify([{
		"filename":i,
		"size":os.stat(i).st_size if os.path.isfile(i) else len(os.listdir(i))} for i in os.listdir()
	])

@app.route('/')
def main_page():
	return render_template("index.html")



@app.route('/size/<filename>/')
def filename_sized(filename):
	return """
	{} - <h1 class="ok"></h1>

	<script src="/static/dkfgnd.js">
	</script>
	<script>
	get("{}");
	</script>
	""".format(filename,filename)

if __name__ == '__main__':
	app.debug = True
	app.run(host="127.0.0.1",port = 80)