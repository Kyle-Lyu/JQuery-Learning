from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("$.ajax().html")


@app.route('/ajax_text', methods=['GET', 'POST'])
def ajax_text():
    # 获取数据
    name = request.values["name"]
    email = request.values["email"]
    # 返回字符串
    result = "用户姓名为" + name + "，用户邮箱为" + email
    return result


@app.route('/ajax_json', methods=['GET', 'POST'])
def ajax_json():
    name = request.values["name"]
    email = request.values["email"]
    # 返回json格式数据
    result = {"name": name, "email": email}
    return result


if __name__ == '__main__':
    app.run(port=5003, debug=True)
