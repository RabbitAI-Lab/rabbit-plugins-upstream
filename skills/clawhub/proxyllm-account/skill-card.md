## Description: <br>
Gives an agent guided steps to create and configure a ProxyLLM account, handle the paid activation flow, mint routing keys, wire provider lanes, and use ProxyLLM as an OpenAI-compatible gateway. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericslab](https://clawhub.ai/user/ericslab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when they want an agent to set up managed LLM gateway access, create ProxyLLM routing keys, configure fallback provider lanes, and point OpenAI-compatible clients at the gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may create and manage a paid ProxyLLM account and sensitive API keys with broad authority. <br>
Mitigation: Require explicit operator confirmation before signup, payment, token storage, key creation, provider-lane changes, or subscription-seat use. <br>
Risk: Account tokens and routing keys can expose management or model-access authority if mishandled. <br>
Mitigation: Treat sk_ and pllm_ values as secrets, store them only in approved secret storage, set monthly budgets on routing keys, and revoke unused keys. <br>
Risk: Provider lanes can use the operator's ChatGPT or Codex subscription capacity and may be subject to those providers' terms. <br>
Mitigation: Confirm the operator understands the monthly cost, capacity impact, and terms before connecting subscription-backed lanes. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/ericslab/skills/proxyllm-account) <br>
- [ProxyLLM](https://proxyllm.ai) <br>
- [ProxyLLM machine manifest](https://proxyllm.ai/auth.md) <br>
- [ProxyLLM OpenAPI specification](https://proxyllm.ai/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and environment variable configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides creation and handling of account tokens, routing keys, provider-lane configuration, budgets, and OpenAI-compatible endpoint settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
