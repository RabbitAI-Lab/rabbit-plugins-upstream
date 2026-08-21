---
name: ClawCode Lens
slug: clawcode-lens
version: 1.0.1
description: "Explain code in any language with structured syntax/logic breakdown, local security scan, and improvement suggestions. Local tools are private and fast. ⚠️ OPTIONAL premium deep scan uses the paid x402 API (X402_API_KEY, USDC) — sends selected source files to an external service and costs money."
metadata: {"clawdbot":{"emoji":"💻","requires":{"bins":["python3"],"env":["X402_API_KEY"],"network":["https://show-zum-anyway-sanyo.trycloudflare.com"]},"permissions":{"exec":["python3"],"files":["<scanned files>"],"network":["https://show-zum-anyway-sanyo.trycloudflare.com"],"notes":"Local tools (explain, security_scan, improve) run 100% locally — no network. The OPTIONAL premium deep scan (/v1/code-scan) uploads the selected source file + X402_API_KEY to the x402 API (PAID, USDC on Ethereum). Do not use premium on confidential code."}}}
---

# ClawCode Lens

Code explanation and analysis tool — inspired by Dify Code Interpreter, **improved**:

## 🆕 Unique features (not in the original)

### Feature 1: Runs 100% LOCALLY — no external API required
The original requires a Dify server + Ollama model + API key. ClawCode Lens analyzes
code directly with structured rules — works offline, free and instantly:

```bash
python3 scripts/explain.py code.py --lang python
python3 scripts/explain.py main.js --lang javascript --detail
```

### Feature 2: Security scanning (local)
Finds vulnerabilities: hardcoded keys, SQL injection, `eval()` misuse, unsafe
`exec` calls, weak passwords, unsafe imports:

```bash
python3 scripts/security_scan.py code.py --out report.md
```

### Feature 3: Improvement suggestions
Gives concrete, prioritized suggestions: complexity, repeated code, missing error handling,
performance bottlenecks and best practices — with code examples:

```bash
python3 scripts/improve.py code.py --out suggestions.md
```

---

## How to use

### Explain code (structured)
```bash
python3 scripts/explain.py file.py --lang python
# Output: overview → key functions → logic flow → edge cases
```

### Supported languages
Python, JavaScript/TypeScript, C/C++, Java, C#, Go, Rust, SQL, Bash, PHP, Ruby — auto-detected from file type.

### Combine everything in one call
```bash
python3 scripts/explain.py app.py --security --improve --out full-report.md
```

## 💰 Premium: Deep security scan (x402 pay-per-call)

Get a deeper scan via the paid x402 API:

```bash
# 1) Get an API key: send USDC (Ethereum) to the wallet, then POST /v1/purchase
export X402_API_KEY=***   # key issued after on-chain verified payment

# 2) Deep scan (PAID call — uploads your code + costs per call)
python3 scripts/code_scan.py app.py
```

- **Payment**: USDC on Ethereum to `0xafd1c6bC2B35152f30E3D0dBE99eE1d40E5a5CF8`
- **Price**: $0.005/call · $25/mo
- ⚠️ Paid call — each run charges your key AND uploads the selected source file to the external API. **Do not use on confidential/proprietary code.**
- 🔒 **PRIVACY:** the premium call sends your source code + API key to an external service. The local tools above never leave your machine.

## Example output (security scan)

```text
🔒 Security scan: app.py
  [CRITICAL] Line 12: API key hardcoded — use env var
  [HIGH]    Line 45: SQL string built with f-string — injection risk
  [INFO]    Line 78: eval() — avoid unless strictly necessary
```

## Feedback
- Helpful? → `clawhub star clawcode-lens`
