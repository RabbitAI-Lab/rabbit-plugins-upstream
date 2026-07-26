## Description: <br>
Local-first LLM Prompt Firewall for MCP tools, AI agents, and gateways. Audits prompts before tool use; detects prompt injection, jailbreak attempts, developer-mode bypasses, hidden-system-prompt extraction, and API key leakage; returns structured PASS or BLOCK decisions with detector, risk level, reason, and optional semantic score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security engineers use this skill as a preflight prompt-auditing layer before user content reaches MCP tools, coding agents, research agents, AI gateways, shells, browsers, code interpreters, or downstream model providers. It returns structured PASS or BLOCK decisions for prompt injection, jailbreak, hidden-system-prompt extraction, and common secret-leakage risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a prompt preflight layer, not a complete security boundary for high-privilege agent workflows. <br>
Mitigation: Pair it with MCP and tool allowlists, provider-side safety settings, output filtering, rate limits, request logging policies, abuse monitoring, and human review for high-risk workflows. <br>
Risk: The first semantic run may attempt to download the sentence-transformer model unless a local model path or offline mode is configured. <br>
Mitigation: Pin dependencies, pre-cache the model, configure a local model path, and set GENAI_SECURITY_LOCAL_ONLY=1 where network fetches are not acceptable. <br>
Risk: Prompt text or secrets may be exposed through terminal output or wrapper logs even though the scanner does not intentionally store requests. <br>
Mitigation: Avoid logging raw prompts in integrations and store only suggested_action, detector, and coarse risk_level where possible. <br>
Risk: Static and semantic detection can produce false positives or false negatives on adversarial or unfamiliar wording. <br>
Mitigation: Tune GENAI_SECURITY_THRESHOLD, maintain the jailbreak template list, and review decisions before using the skill as a gate for privileged actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/margaretzybgl/skills/genai-security-gateway) <br>
- [Security Policy](references/security-policy.md) <br>
- [Jailbreak Templates](references/jailbreak_templates.json) <br>
- [Test Prompts](references/test_prompts.json) <br>
- [Related ClawHub Skill: Optimize Prompt](https://clawhub.ai/margaretzybgl/skills/optimize-prompt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON PASS or BLOCK audit results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audit results include is_safe, risk_level, reason, suggested_action, detector, semantic_score, semantic_threshold, semantic_timeout_seconds, and matched_template when available.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
