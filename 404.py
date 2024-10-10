import os
import threading
from flask import Flask, render_template, request

app = Flask(__name__)

def stress_cpu():
    while True:
        [x**2 for x in range(1000000)]

def stress_ram():
    memory_hog = []
    while True:
        memory_hog.append(os.urandom(10**6))

def run_stress():
    cpu_thread = threading.Thread(target=stress_cpu)
    ram_thread = threading.Thread(target=stress_ram)
    cpu_thread.start()
    ram_thread.start()

@app.route('/')
def index():
    return render_template('trap.html')

@app.route('/run', methods=['POST'])
def run():
    run_stress()
    return "uwu stressing cpu & ram rn!"

if __name__ == '__main__':
    app.run(debug=True)
