# Claude Model Comparison Cheatsheet

| Model Family | Canonical API Model ID | Best Use Cases | Cost Profile |
| :--- | :--- | :--- | :--- |
| **Haiku 5.5** | `claude-haiku-5-5` | Fast lightweight tasks, classification, rapid API responses, budget testing | 🟢 Lowest |
| **Sonnet 5.5** | `claude-sonnet-5-5` | Primary workhorse: coding, complex reasoning, multimodal tasks, tool use | 🟡 Balanced |
| **Opus 5.5** | `claude-opus-5-5` | Maximum intelligence: frontier reasoning, deep synthesis, complex agent workflows | 🔴 Highest |

---

### Tips for Developers
- When prototyping or writing test cases in notebooks, default to `claude-haiku-5-5` to preserve credits.
- For production pipelines needing balanced intelligence and latency, use `claude-sonnet-5-5`.
