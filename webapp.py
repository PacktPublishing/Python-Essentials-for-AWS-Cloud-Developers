from flask import Flask

def say_hello(username = "Serkan"):
    return '<p>Hello %s!</p>\n' % username

text = '''
    <p><em>Hint</em>: Rest web service! Append a username
    to the URL </p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + text + footer_text))

# add a rule when the page is accessed with a name 
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    application.run()
