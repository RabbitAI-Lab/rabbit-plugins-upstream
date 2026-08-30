# Integrations — one skill, every agent runtime

Everything here wraps the **same** contract:

```
python3 scripts/forge.py <command> [flags]      # or: --stdin with a JSON job
→ stdout: exactly one JSON document
→ stderr: human-readable progress only
→ exit:   0 ok · 1 contract/QA fail · 2 usage · 3 deps · 4 no provider · 5 interrupted
```

Because every runtime below funnels into that single path, they all produce the
same artifacts. No runtime gets its own bespoke behaviour.

| File | Purpose |
|---|---|
| `tool-spec.json` | One JSON Schema, reused as an OpenAI function, Anthropic tool, Gemini functionDeclaration and MCP `inputSchema` |
| `mcp_server.py` | Dependency-free MCP server over stdio |
| `adapters.py` | Python glue for LangChain, CrewAI, AutoGen, LlamaIndex, OpenAI Agents, n8n, CI |

Always start with `doctor` — it reports what is installed and which models are reachable.

---

## Plain shell / cron / Makefile

```bash
python3 scripts/forge.py doctor
python3 scripts/forge.py run --pdf lecture.pdf --work out --title 'روان‌شناسی' --maximum
echo '{"command":"run","pdf":"lecture.pdf","work":"out","maximum":true}' \
  | python3 scripts/forge.py --stdin
```

## Python (any framework, or none)

```python
from integrations.adapters import run
print(run("doctor")["verdict"])
result = run("run", pdf="lecture.pdf", work="out", maximum=True)
print(result["status"], result.get("html"))
```

## MCP hosts — Claude Code, Claude Desktop, Cursor, Windsurf, Zed, Continue

```json
{
  "mcpServers": {
    "persian-pdf-studyguide-forge": {
      "command": "python3",
      "args": ["/abs/path/to/skill/integrations/mcp_server.py"],
      "env": { "ANTHROPIC_API_KEY": "..." }
    }
  }
}
```

Verify it by hand:

```bash
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' \
 | python3 integrations/mcp_server.py
```

## OpenAI — function calling / Agents SDK / Codex CLI

```python
from integrations.adapters import openai_tool_spec, run
tools = [openai_tool_spec()]
# when the model calls the tool:
output = run(**json.loads(tool_call.function.arguments))
```

## Anthropic — tool use

```python
from integrations.adapters import anthropic_tool_spec, run
resp = client.messages.create(model="claude-sonnet-4-5",
                              tools=[anthropic_tool_spec()], messages=[...])
```

## Gemini — function declarations

```python
from integrations.adapters import gemini_function_declaration, run
tools = [{"function_declarations": [gemini_function_declaration()]}]
```

(`additionalProperties` and `default` are stripped automatically — Gemini's
schema dialect rejects them.)

## LangChain / LangGraph

```python
from integrations.adapters import as_langchain_tool
agent = create_react_agent(llm, tools=[as_langchain_tool()])
```

## CrewAI

```python
from integrations.adapters import as_crewai_tool
Agent(role="Study guide builder", tools=[as_crewai_tool()], llm=llm)
```

## AutoGen

```python
from integrations.adapters import as_autogen_function
spec = as_autogen_function()
register_function(spec["function"], caller=assistant, executor=user_proxy,
                  name=spec["name"], description=spec["description"])
```

## LlamaIndex

```python
from integrations.adapters import as_llamaindex_tool
agent = ReActAgent.from_tools([as_llamaindex_tool()], llm=llm)
```

## n8n / Zapier / any shell-command node

```python
from integrations.adapters import n8n_execute_command
print(n8n_execute_command("run", pdf="lecture.pdf", work="out"))
```

## GitHub Actions / CI

```yaml
- name: Forge self-test
  run: |
    sudo apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-fas tesseract-ocr-eng
    python3 -m pip install -r requirements.txt
    python3 scripts/forge.py selftest
  env:
    FORGE_MOCK: "1"      # deterministic, no keys, no network
```

---

## Environment conventions

Any **one** of these makes the skill work — no config file needed:

```bash
OPENAI_API_KEY  ANTHROPIC_API_KEY  GEMINI_API_KEY  GROQ_API_KEY
OPENROUTER_API_KEY  MISTRAL_API_KEY  COHERE_API_KEY  DEEPSEEK_API_KEY
TOGETHER_API_KEY  FIREWORKS_API_KEY  XAI_API_KEY  ZAI_API_KEY  HF_TOKEN
OLLAMA_HOST=http://localhost:11434          # local, no key
LOCAL_OPENAI_BASE_URL=http://localhost:8000/v1   # vLLM / LM Studio / llama.cpp
FORGE_MOCK=1                                 # fully offline, deterministic
```

Tuning: `<PROVIDER>_MODEL`, `<PROVIDER>_BASE_URL`, `FORGE_SEED`,
`FORGE_TIMEOUT`, `FORGE_CACHE_DIR`, `FORGE_VERBOSE=0`.

**Key handling:** read from the environment at call time only. Never printed,
never cached, never written to an artifact, and redacted from all error output.

---

## Contract rules for integrators

1. **Parse stdout, never stderr.** stdout is always one JSON document.
2. **Branch on the exit code**, not on log text.
3. **Re-invocation is safe.** Every stage caches; re-running a finished stage
   is a no-op that returns the previous result.
4. **`run` may pause.** Without `--auto-sessions` it returns
   `status: PAUSED_FOR_SESSION_REVIEW` and exit 0 — that is success, and it is
   asking for human review of session boundaries. Honour it; boundaries chosen
   by a model are marked unreviewed.
5. **Never merge the three layers.** `extraction/evidence.json` (raw),
   `corrections/final.json` (reconstruction) and `enrichment/all.json` (AI study
   aids) are deliberately separate. Do not present AI additions as source text.
6. **Authorization is the caller's responsibility.** Only process material the
   operator is entitled to use.
