# Claude API Error Codes & Handling Reference

| HTTP Status | Exception Class in Python SDK | Cause | Recommended Action |
| :--- | :--- | :--- | :--- |
| **400** | `anthropic.BadRequestError` | Malformed JSON, missing mandatory parameter (`max_tokens`), or bad messages structure | Validate payload structure and parameter names |
| **401** | `anthropic.AuthenticationError` | Missing, incorrect, or revoked API key | Check `.env` file and API key credentials in console |
| **403** | `anthropic.PermissionDeniedError` | Account restricted or insufficient permissions for specific feature | Verify tier / organization access |
| **404** | `anthropic.NotFoundError` | Invalid model identifier or non-existent endpoint | Verify canonical model ID (e.g. `claude-haiku-5-5`) |
| **429** | `anthropic.RateLimitError` | Rate limits exceeded (TPM: tokens per minute, or RPM: requests per minute) | Implement exponential backoff or request tier increase |
| **500 / 529**| `anthropic.InternalServerError` / `APIStatusError` | Anthropic servers overloaded or temporary outage | Retry request with jittered backoff |

---

### Python Robust Exception Handling Template

```python
import anthropic

client = anthropic.Anthropic()

try:
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=500,
        messages=[{"role": "user", "content": "Hello!"}]
    )
except anthropic.APIConnectionError:
    print("Network issue: Unable to reach Anthropic servers.")
except anthropic.RateLimitError:
    print("Hit rate limit: Backing off...")
except anthropic.APIStatusError as e:
    print(f"API Error ({e.status_code}): {e.message}")
```

