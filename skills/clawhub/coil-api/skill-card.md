## Description:

Use Coil's CLI and API for agent-operated outbound recipes, durable runs, lead management, automations, provider integrations, feedback, and runtime discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to install and authenticate the Coil CLI, discover available Coil runtime capabilities, and operate Coil workflows for recipes, durable runs, leads, automations, integrations, and feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Coil operations can use organization-scoped API keys and provider credentials.

Mitigation: Provide Coil and provider secrets through a runtime secret manager or stdin, and avoid placing them in command arguments, logs, issue bodies, or recipe inputs.

Risk: Provider-backed workflows can spend credits or trigger outbound business actions.

Mitigation: Review spend-confirming commands before execution and require deliberate human approval for admin-session actions such as publishing, deleting, policy changes, credential rotation, and ambiguous-effect reconciliation.

Risk: Queued or running durable runs may be mistaken for completed lead generation results.

Mitigation: Inspect or wait for durable recipe-run status before claiming usable leads or acting on run outputs.

## Reference(s):

- [Coil API Endpoints](references/api-endpoints.md)
- [Coil API Fields](references/api-fields.md)
- [Coil Homepage](https://www.usecoil.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API details, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON-oriented CLI workflows and local API reference files for machine-readable operation guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
