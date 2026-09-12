## Description:

Registers a new Openclaw AI Agent via the AgentAuthentication API for provisioning a new agent account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kingdestinythe1st](https://clawhub.ai/user/kingdestinythe1st)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to collect validated registration details and create Openclaw AI Agent accounts through the disclosed AgentAuthentication API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration requests include credentials and personal contact information.

Mitigation: Confirm with the user before sending registration details, avoid password reuse, and verify that the endpoint is the trusted Openclaw service.

Risk: Unexpected payload fields may be rejected by the API validation layer.

Mitigation: Send only the documented registration fields and correct validation errors before retrying.

## Reference(s):

- [Authentication skill page](https://clawhub.ai/kingdestinythe1st/skills/agent-authentication)
- [Openclaw agent registration endpoint](https://us-central1-openclaw-authentication-646b0.cloudfunctions.net/api/v1/agents/register)
- [Publisher profile](https://clawhub.ai/user/kingdestinythe1st)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with JSON payload examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API response interpretation for registration success, validation errors, conflicts, or server failures.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
