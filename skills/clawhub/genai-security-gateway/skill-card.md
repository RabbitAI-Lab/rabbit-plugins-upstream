## Description: <br>
Local-first LLM Prompt Firewall for MCP tools, AI agents, and gateways. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to audit prompts before they reach MCP tools, agents, shells, browsers, code interpreters, or LLM gateways. It returns structured pass or block decisions for prompt injection, jailbreak, and common secret-leakage checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First semantic use can trigger model download behavior and dependency execution. <br>
Mitigation: Review and pin dependencies before installation; pre-cache or provide a local model path and set GENAI_SECURITY_LOCAL_ONLY=1 for offline or sensitive deployments. <br>
Risk: Prompt audit results are a preflight signal, not a complete security boundary. <br>
Mitigation: Pair the skill with MCP and tool allowlists, provider safety settings, output filtering, request logging policies, rate limits, abuse monitoring, and human review for high-risk workflows. <br>
Risk: CLI or wrapper logs may expose sensitive prompt text during secret-leakage checks. <br>
Mitigation: Avoid logging raw prompts and store only coarse fields such as suggested_action, detector, and risk_level where possible. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/margaretzybgl/skills/genai-security-gateway) <br>
- [Security Policy](references/security-policy.md) <br>
- [Jailbreak Templates](references/jailbreak_templates.json) <br>
- [Test Prompts](references/test_prompts.json) <br>
- [Optimize Prompt Related Skill](https://clawhub.ai/margaretzybgl/skills/optimize-prompt) <br>


## Skill Output: <br>
**Output Type(s):** [json, guidance, shell commands, configuration] <br>
**Output Format:** [JSON audit result with optional Markdown and bash usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The primary audit result includes is_safe, risk_level, reason, suggested_action, detector, semantic_score, semantic_threshold, semantic_timeout_seconds, and matched_template.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
