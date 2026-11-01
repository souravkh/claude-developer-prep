# Claude Model Comparison Cheatsheet

| Model Family | Canonical Model ID | Context Window | Max Output Tokens | Best Use Cases |
| :--- | :--- | :--- | :--- | :--- |
| **Claude 3.5 Haiku** | `claude-3-5-haiku-latest`<br>`(claude-3-5-haiku-20241022)` | 200k | 8,192 | Fast classification, tagging, rapid API responses, budget testing |
| **Claude 3.5 Sonnet** | `claude-3-5-sonnet-latest`<br>`(claude-3-5-sonnet-20241022)` | 200k | 8,192 | Coding, multimodal reasoning, tool use, complex data analysis |
| **Claude 3.7 Sonnet** | `claude-3-7-sonnet-latest`<br>`(claude-3-7-sonnet-20250219)` | 200k | 8,192 (up to 64k thinking) | Hybrid reasoning, frontier math & logic, extended thinking |
| **Claude 3 Opus** | `claude-3-opus-latest`<br>`(claude-3-opus-20240229)` | 200k | 4,096 | Complex qualitative research, long-form creative writing |

---

### Tips for Developers
- Always prefer `-latest` aliases for convenience, or pinned dated IDs for reproducible production pipelines.
- When prototyping or writing test cases in notebooks, default to `claude-3-5-haiku-latest` to preserve credits.

