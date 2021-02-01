from flask import Flask,redirect,render_template,request, redirect, url_for
from run_allcase import auto_run
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/list',methods=['GET', 'POST'])
def list():
    return render_template("main.html")

#接口自动化测试主页面
@app.route('/inferauto', methods=['GET', 'POST'])
def interauto():
    return  render_template('inferauto.html')

#接口自动化测试主页面
@app.route('/inferautostart', methods=['GET', 'POST'])
def inferautostart():
    p=auto_run()
    return  render_template('inferauto.html',name=p['测试结果'],filename=p['报告名称'])

if __name__ == '__main__':
    # app.run(debug=True)
    http_server= WSGIServer(("0.0.0.0",5000),app)
    http_server.serve_forever()