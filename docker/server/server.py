from flask import Flask
from flask import request
import uuid
import subprocess
from subprocess import Popen
import simplejson as json

app = Flask(__name__)

@app.route('/')
def index():
	return "hello world"

@app.route('/api/v0/workflow', methods=['POST'])
def api_v0_workflow():
	uid = str(uuid.uuid4())
	INFILE_PATH  = "/dev/shm/input.json"
	OUTFILE_PATH = "/dev/shm/output.json"

	payload = request.get_data()

	
	with open(INFILE_PATH, "wb") as infile
:		infile.write(payload)
	cmd = '/knime_3.7.1/knime -nosplash -reset -nosave -application org.knime.product.KNIME_BATCH_APPLICATION -workflowFile=/worker/workflow.knwf'.split()
	process = Popen(cmd)

	process.wait(timeout=100)
	with open(OUTFILE_PATH) as outfile:
		output=outfile.read()

	# try:
	# 	process.wait(timeout=100)
	# 	with open(OUTFILE_PATH):
	# 		output=myfile.read()

	# except subprocess.TimeoutExpired:
	# 	process.terminate()
	# 	output = json.dumps({"error": "timeout"})
	# 	response = app.response_class(
	# 		response = output,
	# 		status=500,
	# 		mimetype="application/json")
	# 	return response

	response = app.response_class(
		response = output,
		status=200,
		mimetype="application/json")

	return response


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)