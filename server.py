from flask import Flask, render_template, request, flash, redirect, session, jsonify
from model import connect_to_db, db, User, Event, Event_Cocktail
import api
import requests

app = Flask(__name__)
app.secret_key = 'FLATTEN THE CURVE'

@app.route('/')
def homepage():
    """Show homepage."""
    return render_template('homepage.html')