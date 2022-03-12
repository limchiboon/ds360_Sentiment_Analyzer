# Full Stack Data Scientist Demo

## Install Flask

```bash
pip install flask
```

## Our first app Hello.py

Create a file `hello.py` with the following code.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## Run our app 

### For Mac

```bash
export FLASK_APP=hello.py FLASK_ENV=development
flask run
```

### For Windows Command Prompt

```bash
set FLASK_APP=hello.py 
set FLASK_ENV=development
flask run
```

### For PowerShell

```bash
$env:FLASK_APP = "hello"
$env:FLASK_ENV = "development"
flask run
```

> If your app doesn't show up, try to use `python -m flask run`, sometimes it is due to the path configuration.

If you see the following, means we have successfully launched our app!

```
(ds360) ➜  ds360 flask run
 * Serving Flask app 'hello.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 633-980-227
 ```
 
 ## Add sentiment analysis function
 
 create a new route name `sentiment` and add the following code to `hello.py`:
 
 ```python
@app.route("/sentiment")
def analyze():
  s = "Today is the voting day. I am so excited to vote."
  analyzer = SentimentIntensityAnalyzer()
  score = analyzer.polarity_scores(s)
  return score
```

Restart our server. Stop the Flask app (using Ctrl-c), and rerun the `flask run` command.

> If it complains that NLTK is not installed, run `pip install nltk` before restarting.

After restarting our Flask app, open `http://127.0.0.1:5000/sentiment` in your browser. You should receive the following output.

```
{
  "compound": 0.4795, 
  "neg": 0.0, 
  "neu": 0.743, 
  "pos": 0.257
}
```

## Analyze sentiment from URL query string

First of all, add `request` to the import. 

```python
from flask import Flask, request
```

Update our `analyze()` method with the following code:

```python
@app.route("/sentiment")
def analyze():
  args = request.args
  s = args.get("s")
  
  analyzer = SentimentIntensityAnalyzer()
  score = analyzer.polarity_scores(s)
  return score
```

Open [http://127.0.0.1:5000/sentiment?s=today%20is%20the%20voting%20day%20and%20I%20am%20excited](http://127.0.0.1:5000/sentiment?s=today%20is%20the%20voting%20day%20and%20I%20am%20excited) in your browser. And you see the following outputs.

```json
{
  "compound": 0.34, 
  "neg": 0.0, 
  "neu": 0.745, 
  "pos": 0.255
}
```


 
# References 
- https://flask.palletsprojects.com/en/2.0.x/
