from flask import *
import os


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def main_page():
	if request.form.get("val"):
		try:
			os.system("pip install {}".format(
				request.form.get("val")
			))
			text = "Download if y"
		except:
			pass

		return render_template("index.html",desc=text)

	return render_template("index.html")



if __name__ == '__main__':
	app.debug = True
	app.run(host="localhost",port=80)