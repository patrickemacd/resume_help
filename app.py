from flask import Flask, render_template, request, jsonify
from resume_optimizer import ResumeOptimizer
import traceback

app = Flask(__name__)

# Initialize optimizer once
optimizer = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    global optimizer
    try:
        if optimizer is None:
            optimizer = ResumeOptimizer()
        
        data = request.json
        jd_text = data.get('jd_text', '').strip()
        resume_text = data.get('resume_text', '').strip()
        
        if not jd_text or not resume_text:
            return jsonify({'error': 'Both job description and resume text are required'}), 400
        
        results = optimizer.optimize_from_text(jd_text, resume_text)
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e), 'traceback': traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)