## Description:

Connects agents to user-authorized third-party apps through Maton for API requests and approved app operations or automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users use the skill to read or update information in services they have connected, and to manage approved integrations and hosted automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected apps can expose data and allow changes; optional hosted automation can continue acting after setup.

Mitigation: Connect only services and permissions needed, prefer read-only access, and explicitly confirm writes and automation before they run.

Risk: Event destinations can forward data persistently, while local event handlers process content that may come from untrusted sources.

Mitigation: Review and approve each destination and the data it forwards; use a narrow, user-reviewed handler and stop or remove automation when it is no longer needed.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Documentation](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API calls, Text, JSON, Shell commands, Code, Configuration guidance]

**Output Format:** [API requests and responses, with shell commands, JSON examples, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a Maton account; access is limited to connected services and authorized permissions.]

## Skill Version(s):

1.2.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
