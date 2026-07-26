## Description: <br>
A.I. Smart Router selects among Claude, GPT, Gemini, and Grok using semantic domain scoring, context-overflow checks, fallback chains, HITL gates, and cost-aware routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[c0nspic0us7urk3r](https://clawhub.ai/user/c0nspic0us7urk3r) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to route prompts across enabled AI providers based on task type, context size, risk domain, model availability, and cost. It can also provide routing visibility, fallback notices, status summaries, and configuration guidance for OpenClaw-style multi-provider workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts may be routed or retried across different enabled AI providers without the user inspecting each provider choice. <br>
Mitigation: Use the skill with non-sensitive workflows, restrict enabled providers to approved services, and review live versus dry-run routing before deployment. <br>
Risk: Routing telemetry and state may persist locally and reveal prompt categories, model selections, failures, or usage patterns. <br>
Mitigation: Periodically inspect or purge the configured OpenClaw router logs and state files, and avoid routing confidential or restricted data unless retention is acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/c0nspic0us7urk3r/skills/smart-router) <br>
- [README](README.md) <br>
- [Model Capabilities & Pricing Reference](references/models.md) <br>
- [Security Best Practices for Model Routing](references/security.md) <br>
- [Smart-Router State Summary](STATE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, routing notices, JSON and JSONL state records, and Python or shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist routing decisions, circuit-breaker state, and rate-limit state under user-configured OpenClaw paths.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
