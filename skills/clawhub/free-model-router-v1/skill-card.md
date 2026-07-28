## Description: <br>
Routes OpenClaw model requests through a local free-model router that helps configure providers, choose models, fail over, and diagnose availability issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laodao-agent](https://clawhub.ai/user/laodao-agent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and developers use this skill to configure a local model-routing proxy, add provider API keys, select primary and fallback models, and recover from provider or model outages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The persistent local router stores provider keys and its admin surface may expose secrets or broad local controls. <br>
Mitigation: Use only in a trusted local environment, restrict local access, review the admin panel before use, and avoid valuable provider keys until authentication and key redaction controls are confirmed. <br>
Risk: Prompts and model responses are forwarded to external model providers selected through the router. <br>
Mitigation: Do not route sensitive prompts unless the selected provider's data handling and terms are acceptable for the user's workload. <br>
Risk: The updater code path is high impact for a local agent skill that can run commands and modify configuration. <br>
Mitigation: Review update behavior and release integrity before enabling or executing update-related actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/laodao-agent/skills/free-model-router-v1) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Event System](references/event-system.md) <br>
- [Idempotency Guide](references/idempotency.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May instruct the agent to run local Node.js CLI commands and guide OpenClaw configuration changes.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
