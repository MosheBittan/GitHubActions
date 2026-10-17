from flask import Flask, request, send_file
app = Flask(__name__)

@app.route('/download')
def download():
    filename = request.args.get('file')        # קלט מהמשתמש, למשל ?file=report.pdf
    path = "/var/www/files/" + filename         # בונים נתיב
    return send_file(path)                      # מחזירים את הקובץ

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
