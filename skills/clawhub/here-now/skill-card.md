## Description:

here.now lets agents publish websites and files to live URLs, manage access-controlled Sites and workspaces, and use private Drive storage through bundled shell helpers or the here.now API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to publish generated sites or files, update existing here.now Sites, configure access controls, publish to team workspaces, and manage private Drive files for agent handoff or persistence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected files, publish them to live URLs, and modify site access settings.

Mitigation: Review selected files and access mode before publishing, password-protecting, restricting, or overwriting a Site.

Risk: The skill can store and reuse a here.now API key from disk.

Mitigation: Confirm credential persistence with the user and keep the credentials file private with restrictive permissions.

Risk: The skill can manage private Drive files and create scoped Drive share tokens.

Mitigation: Use narrow path prefixes, short token lifetimes, and explicit confirmation before sharing or deleting Drive content.

Risk: A non-default API base URL could receive bearer credentials if explicitly allowed.

Mitigation: Keep the default here.now API base unless the user intentionally approves a trusted alternative endpoint.

## Reference(s):

- [here.now documentation](https://here.now/docs)
- [here.now OpenAPI specification](https://here.now/openapi.json)
- [ClawHub skill page](https://clawhub.ai/adamludwin/skills/here-now)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API examples, URLs, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce live site URLs, access-control guidance, Drive commands, and credential storage instructions.]

## Skill Version(s):

1.27.0 (source: server release metadata and artifact/SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
