# Resume Optimizer - Web Interface

I have built this AI workflow to help me apply for jobs in a more efficient manner. I've been taking some courses on implementing LLMs within my code and thought this could be a cool way to help A) learn more B) help my job search. Although simple, it has helped me fine-tune my resume in respect to the job description that I am applying for. It utilizes a very simple flask app for input. Feel free to change the model and prompt. I am currently using gpt-4o-mini.


## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your API Key in `.env` file:**
   ```bash
   cp .env.example .env
   # Edit .env and replace with your actual API key
   ```
   - Get your API key from [OpenAI Platform](https://platform.openai.com/docs/quickstart)
   - **⚠️ NEVER commit your .env file to GitHub!**

3. **Start the web server:**
   ```bash
   python app.py
   ```

4. **Open browser to:** Your terminal will output the url to paste. Will run on local host.

5. **Use the interface:**
   - Paste your resume text in the left panel
   - Paste job description in the right panel
   - Click "Optimize Resume"
   - Wait 30-60 seconds for results

## Features

- **Web Interface** - Easy copy/paste input, no file management
- **Real-time Processing** - See results in browser.
- **ATS Expert Analysis** -  Prompt engineer to take on persona of resume expert.
- **Detailed Results** - Key requirements, optimized resume, improvements

## Files

- `app.py` - Web server (run this)
- `resume_optimizer.py` - Core optimization logic
- `templates/index.html` - Web interface
- `requirements.txt` - Python dependencies

## Legacy Command Line

Still available for file-based processing:
```bash
python resume_optimizer.py
```

Simple, fast, and effective. 🚀