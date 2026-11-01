# Claude Developer Preparation

A hands-on workspace and knowledge base for mastering the Anthropic Claude API, prompt engineering, tool use, agent architectures, and production LLM development.

---

## 📁 Repository Structure

```text
claude-developer-prep/
│
├── .env                         # Local API credentials (ignored by git)
├── .env.example                 # Environment template
├── .gitignore                   # Git exclusion rules
├── requirements.txt             # Project dependencies (anthropic, python-dotenv)
├── README.md                    # Workspace guide (this file)
│
├── 01_basics_and_setup/         # Core basics & initial API call
│   ├── README.md                # Notes: Messages API rules, model tiers, common pitfalls
│   ├── 01_first_api_call.ipynb  # Step-by-step instructional notebook
│   └── 01_first_api_call.py     # Standalone Python script
│
└── cheatsheets_and_notes/       # Quick-lookup reference guides
    ├── model_comparison.md      # Specs, context windows, and cost profiles
    └── error_codes_cheatsheet.md# API HTTP status codes and SDK exceptions
```

---

## 🚀 Setup & Getting Started

### 1. Install Dependencies
Ensure your virtual environment is active, then install the required packages:
```bash
pip install -r requirements.txt
```

### 2. Configure Credentials
Add your key inside a `.env` file at the root of the project (refer to `.env.example`):
```env
ANTHROPIC_API_KEY=your_actual_api_key_here
```

### 3. Explore Module 01
Navigate to [`01_basics_and_setup/`](01_basics_and_setup/):
- **Interactive Guide:** Open [`01_first_api_call.ipynb`](01_basics_and_setup/01_first_api_call.ipynb) in your notebook editor.
- **Python Script:** Review [`01_first_api_call.py`](01_basics_and_setup/01_first_api_call.py) for the standalone script implementation.
- **Topic Notes:** Read [`01_basics_and_setup/README.md`](01_basics_and_setup/README.md) for conceptual fundamentals and common gotchas.

---

## 📖 Quick References
- [Model Comparison Cheatsheet](cheatsheets_and_notes/model_comparison.md)
- [API Error Codes & Handling](cheatsheets_and_notes/error_codes_cheatsheet.md)
