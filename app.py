from flask import Flask, render_template, request

app = Flask(__name__)

# 在每次请求处理之前执行的操作
@app.before_request
def before_request():
    print(f"Handling request for {request.path}")

# 基础模板
@app.route('/')
def index():
    app_root = request.url_root
    print(f"Flask app is running at: {app_root}")
    return render_template('index.html')

# About 页面，继承基础模板
@app.route('/about')
def about():
    # 传递变量到模板
    page_content = get_page_content('about.html')  # 获取关于页面的内容

    return render_template('about.html')

# Projects 页面，继承基础模板
@app.route('/projects')
def projects():
    # 传递变量到模板
    #page_content = get_page_content('projects.html')  # 获取项目页面的内容

    return render_template('projects.html')

# Contact 页面，继承基础模板
@app.route('/computer_science')
def computer_science():
    # 传递变量到模板
    #page_content = get_page_content('cs.html')  # 获取联系页面的内容

    return render_template('cs.html')

@app.route('/mathematics')
def mathematics():
    return render_template('mathematics.html')

@app.route('/math_content')
def math_content():
    return render_template('math_content.html')

@app.route('/game_development')
def game_development():
    return render_template('game_development.html')

# 模拟从文件系统或数据库获取页面内容的函数
def get_page_content(page_name):
    # 这里可以根据实际情况从文件系统、数据库或其他数据源获取页面内容
    # 这里简化为直接读取文件内容，示例中假设文件存放在 templates 目录下
    try:
        with open(f'templates/{page_name}', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f'<p>{page_name} not found.</p>'

if __name__ == '__main__':
    app.run(debug=True)
