from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("$.post().html")


@app.route('/post_text', methods=['POST'])
def post_text():
    # 获取数据
    name = request.values["name"]
    email = request.values["email"]
    # 返回字符串
    result = "用户姓名为" + name + "，用户邮箱为" + email
    return result


@app.route('/post_json', methods=['POST'])
def post_json():
    name = request.values["name"]
    email = request.values["email"]
    # 返回json格式数据
    result = {"name": name, "email": email}
    return result


if __name__ == '__main__':
    app.run(port=5002, debug=True)
