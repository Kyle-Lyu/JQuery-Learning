from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("$.get().html")


@app.route('/get_text', methods=['GET'])
def get_text():
    # 获取数据
    name = request.values["name"]
    email = request.values["email"]
    # 返回字符串
    result = "用户姓名为" + name + "，用户邮箱为" + email
    return result


@app.route('/get_json', methods=['GET'])
def get_json():
    name = request.values["name"]
    email = request.values["email"]
    # 返回json格式数据
    result = {"name": name, "email": email}
    return result


if __name__ == '__main__':
    app.run(port=5001, debug=True)
