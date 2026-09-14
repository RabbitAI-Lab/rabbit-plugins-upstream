## Description:

here.now lets agents publish websites and files to live URLs, manage site access, publish to team workspaces, store private Drive files, and register domains through the here.now service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use here.now to publish generated sites and files, update existing sites, configure access controls, manage private Drive storage, and guide domain-related publishing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drive sharing can expose private files if tokens are broad or long-lived.

Mitigation: Create Drive share tokens only with explicit read or write scope, a narrow path prefix, and a short expiration.

Risk: Persistent credentials and publish state can expose account access or site claim information if mishandled.

Mitigation: Protect ~/.herenow/credentials and .herenow/state.json, avoid committing them, and prefer the credentials file over command-line API key flags.

Risk: Chat-based sign-in code handling gives the agent access to authentication material.

Mitigation: Paste one-time sign-in codes only when the user accepts agent-assisted authentication and the environment is appropriate for handling the code.

Risk: The server security verdict is suspicious due to unsafe defaults around Drive sharing and persistent credentials.

Mitigation: Review the skill before installation and use it only for content intended to be published or stored with here.now.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adamludwin/skills/here-now)
- [here.now documentation](https://here.now/docs)
- [here.now OpenAPI specification](https://here.now/openapi.json)
- [Site creation documentation](https://here.now/docs#create)
- [Domain purchase documentation](https://here.now/docs#buy-domain)
- [Workspace documentation](https://here.now/docs#workspaces)
- [Access control documentation](https://here.now/docs#access-control)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, URLs, and script output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May publish files or sites to live URLs and may store local credential and publish-state files when used with here.now account credentials.]

## Skill Version(s):

1.30.0 (source: server release evidence and skill documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
