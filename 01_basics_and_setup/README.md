# Module 01: Claude Basics & Environment Setup

This folder covers the foundational concepts required to authenticate and query Claude via the official Python SDK.

---

## 1. Key Concepts

### Messages API Architecture
Unlike legacy completion APIs (`prompt: "..."`), Anthropic uses the **Messages API** (`messages: [...]`).
- **Alternating Turns**: Messages must alternate between `user` and `assistant`.
- **System Prompts**: System instructions do **not** go into the `messages` array. They are defined via the dedicated top-level parameter: `client.messages.create(system="...", messages=[...])`.
- **Required `max_tokens`**: Every call requires an explicit token generation ceiling.

### Current Model Families
| Model Tier | API Model ID | Best For | Relative Cost |
| :--- | :--- | :--- | :--- |
| **Haiku 5.5** | `claude-haiku-5-5` | High-volume tasks, quick lookups, cost-conscious dev | 🟢 Lowest |
| **Sonnet 5.5** | `claude-sonnet-5-5` | Complex reasoning, coding, deep agentic tasks | 🟡 Moderate |
| **Opus 5.5** | `claude-opus-5-5` | Maximum intelligence, deep synthesis, complex agent workflows | 🔴 Highest |

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

- [`01_first_api_call.ipynb`](01_first_api_call.ipynb): Interactive, instructional notebook stepping through authentication, payload creation, and response parsing.
- [`01_first_api_call.py`](01_first_api_call.py): Clean, standalone Python script ready to run or integrate into other applications.

---

## 4. Common Gotchas
1. **Model ID Syntax**: Always verify current model IDs (`claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5`).
2. **Missing `max_tokens`**: Omitting `max_tokens` results in an immediate validation error from the SDK.
3. **Empty `.env`**: Always use `load_dotenv(find_dotenv())` so Python searches up directory levels to discover the root `.env`.
