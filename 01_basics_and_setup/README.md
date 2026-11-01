# Module 01: Claude Basics & Environment Setup

This folder covers the foundational concepts required to authenticate and query Claude via the official Python SDK.

---

## 1. Key Concepts

### Messages API Architecture
Unlike legacy completion APIs (`prompt: "..."`), Anthropic uses the **Messages API** (`messages: [...]`).
- **Alternating Turns**: Messages must alternate between `user` and `assistant`.
- **System Prompts**: System instructions do **not** go into the `messages` array. They are defined via the dedicated top-level parameter: `client.messages.create(system="...", messages=[...])`.
- **Required `max_tokens`**: Every call requires an explicit token generation ceiling.

### Model Families Overview
| Model Tier | Identifier | Best For | Relative Cost |
| :--- | :--- | :--- | :--- |
| **Haiku** | `claude-3-5-haiku-latest` | High-volume tasks, quick lookups, cost-conscious dev | 🟢 Lowest |
| **Sonnet** | `claude-3-5-sonnet-latest` / `claude-3-7-sonnet-latest` | Complex reasoning, coding, deep agentic tasks | 🟡 Moderate |
| **Opus** | `claude-3-opus-latest` | Deep synthesis and nuanced writing | 🔴 Highest |

---

## 2. Environment Setup

### 1. Requirements
Install the necessary packages:
```bash
pip install -r ../requirements.txt
```

### 2. Configure `.env`
Place a `.env` file in the root of the repository:
```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

---

## 3. Contents of this Module

- [`01_first_api_call.ipynb`](01_first_api_call.ipynb): Interactive, instructional notebook stepping through authentication, payload creation, and error inspection.
- [`01_first_api_call.py`](01_first_api_call.py): Clean, standalone Python script ready to run or integrate into other applications.

---

## 4. Common Gotchas
1. **Invalid Model Names**: Naming strings like `claude-haiku-5-5` or `haiku-3` don't exist and will throw a `404 Not Found` error.
2. **Missing `max_tokens`**: Omitting `max_tokens` results in an immediate validation error from the SDK.
3. **Empty `.env`**: Always use `load_dotenv(find_dotenv())` so Python searches up directory levels to discover the root `.env`.

