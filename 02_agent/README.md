# Module 02: Agent Loop & Tool Use

This module covers building an autonomous **Agent Loop** with Claude, implementing external tool access (function calling) and multi-turn reasoning.

---

## 1. Key Concepts

### How Tool Use Works in Anthropic SDK

```text
  ┌─────────────────┐
  │   User Prompt   │
  └────────┬────────┘
           │
           ▼
  ┌────────────────────────────────────────────────────────┐
  │  Call Claude Messages API (with tools & conversation)  │◄────────┐
  └────────────────────────┬───────────────────────────────┘         │
                           │                                         │
                           ▼                                         │
                 [ Inspect stop_reason ]                             │
                           │                                         │
            ┌──────────────┴──────────────┐                          │
     "tool_use"                      "end_turn"                      │
            │                             │                          │
            ▼                             ▼                          │
  ┌────────────────────┐        ┌──────────────────┐                 │
  │ Execute local tool │        │  Print & return  │                 │
  │     (run_tool)     │        │   final answer   │                 │
  └─────────┬──────────┘        └──────────────────┘                 │
            │                                                        │
            ▼                                                        │
  ┌───────────────────────────────────────────────┐                  │
  │ Append tool_result to messages conversation   │──────────────────┘
  └───────────────────────────────────────────────┘
```

1. **Tool Declaration**: You provide Claude with tool definitions containing JSON Schema parameters.
2. **Claude Chooses to Call**: Claude pauses generation and returns `stop_reason == "tool_use"`.
3. **Execution**: Your application executes the function locally.
4. **Result Feeding**: You append the result as a `"tool_result"` block under a `"user"` message.
5. **Final Answer**: Claude digests the result and outputs `stop_reason == "end_turn"`.

---

## 2. Contents of this Module

- [`agent_loop.ipynb`](agent_loop.ipynb): Step-by-step interactive tutorial on tool definitions, stop reasons, loop structure, and memory preservation.
- [`agent_loop.py`](agent_loop.py): Standalone Python script implementation with safety iteration caps and intermediate thought logging.

---

## 3. Best Practices
- **Never allow unbounded loops**: Always include a `max_iterations` guard to prevent infinite API calls.
- **Accurate tool descriptions**: Claude selects tools based on the quality of your descriptions and parameter documentation.
- **Support parallel tool use**: Always iterate through all blocks in `response.content`, as Claude can request multiple tools simultaneously.

