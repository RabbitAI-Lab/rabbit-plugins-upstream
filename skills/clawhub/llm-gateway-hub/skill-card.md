## Description:

Helps developers use one gateway to call multiple model providers, manage API keys, and track model spending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only; documentation and theory all rights reserved)

## Use Case:

Developers and teams use this skill to configure a local gateway for multiple model APIs, centralize credentials, and review usage and costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider API keys are stored in a local configuration file.

Mitigation: Restrict file access and keep the configuration out of shared storage and repositories.

Risk: Selected prompts are sent to configured model providers.

Mitigation: Check provider privacy terms and avoid sending sensitive prompts without approval.

Risk: The local hard-budget check may not prevent expensive text requests or high max-token usage.

Mitigation: Set provider-side spending caps and monitor provider billing rather than relying only on the local budget check.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zhaoxinghua09-cell/skills/llm-gateway-hub)
- [Publisher homepage](https://nomos.ai)
- [Gateway configuration template](references/gateway_config.template.json)
- [Guide to adding a provider](references/接入新平台指引.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and JSON configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses and recorded usage depend on the configured provider.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
