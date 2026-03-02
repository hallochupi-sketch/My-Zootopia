# My Zootopia 🦊🐰

My Zootopia is a small Python project that fetches information about animals from a free online API and generates a simple web page to display the results.  
It is built as a learning exercise for working with HTTP APIs, JSON data, and basic HTML generation using Python.

---

## Installation & Configuration

### 1. (Optional but recommended) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # on macOS/Linux
.venv\Scripts\activate      # on Windows
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

This project expects your API Ninjas key to be available as an environment variable (for example `ANIMALS_API_KEY`) or loaded from a `.env` file using `python-dotenv`.

Create a `.env` file in the project root:

```text
ANIMALS_API_KEY=your_api_key_here
```

Make sure the code that loads the API key uses the same variable name.

If your Codio or course template uses a different variable name, update either the code or this section accordingly.

---

## Usage & Project Structure

Ensure your API key is configured as described above.

Run the main script:

```bash
python animals_web_generator.py
```

After the script finishes, open the generated HTML file in your browser.

This is usually created in a folder such as `web/`, `output/`, or the project root, depending on how your template is set up.

Double-click the HTML file or open it via **Open File** in your browser.

If your project asks for the animal name via input in the terminal, follow the on-screen instructions to type the animal you want details for.

---

## Typical Project Structure

```
My-Zootopia/
├─ animals_web_generator.py
├─ template.html        # base HTML template (if provided)
├─ requirements.txt
├─ README.md
└─ .env                 # not committed, contains your API key
```

Your actual structure from the Codio unit may vary slightly; adjust this section to reflect your files.

---

## What You Learn

This project focuses on clarity rather than advanced frameworks and is a good starting point to practice:

* Making GET requests with `requests`
* Handling JSON responses and extracting data
* Filling placeholders in an HTML template
* Working with Git and GitHub (clone, commit, push)

---

## Contributing

This project was created as a learning exercise.

If you’d like to experiment or improve it:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

Suggestions and improvements are welcome.