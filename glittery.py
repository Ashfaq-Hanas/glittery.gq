from flask import Flask, render_template, url_for

app = Flask(__name__)

import pandas as pd
df = pd.read_excel('glittery test sheet.xlsx')
posts = df.to_dict('records')

'''
posts = [
    {
        'img' : 'https://www.himgs.com/imagenes/hello/social/hello-fb-logo.png',
        'link' : 'www.google.com',
        'title' : 'howdy there'
    },
    {
       'img' :  'https://upload.wikimedia.org/wikipedia/en/6/6b/Hello_Web_Series_%28Wordmark%29_Logo.png',
        'title' : 'hello to you too'
    }
]
'''
@app.route('/')
def hello():
    return render_template('home.html', posts=posts)



if __name__ == '__main__':
    app.run(debug=True)