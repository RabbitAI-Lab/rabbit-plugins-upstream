## Description:

here.now lets agents publish websites and files to live URLs, manage access controls, publish to workspaces, and use private Drive storage for persistent files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to publish local files, generated sites, and Drive snapshots to here.now URLs, configure public, password, restricted, or workspace access, and manage private Drive content for handoff or persistence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish selected local files to live here.now URLs, including authenticated permanent sites.

Mitigation: Confirm the intended files and target visibility before publishing, and avoid providing sensitive content unless the access mode is clear.

Risk: The skill can store a here.now API key in ~/.herenow/credentials for authenticated publishing.

Mitigation: Use authenticated mode only when local credential storage is acceptable, keep the credentials file private, and remove the key when it is no longer needed.

Risk: The Drive helper can import, export, share, revoke, remove, and delete private Drive content.

Mitigation: Use narrow path prefixes and short token lifetimes for sharing, and require explicit confirmation for destructive Drive actions.

Risk: Custom base URL options can send credentials away from the default here.now endpoint when explicitly overridden.

Mitigation: Use the default https://here.now endpoint unless there is a specific trusted reason to pass --allow-nonherenow-base-url.

## Reference(s):

- [ClawHub listing for here.now](https://clawhub.ai/adamludwin/skills/here-now)
- [here.now documentation](https://here.now/docs)
- [here.now version history documentation](https://here.now/docs#versions)
- [here.now workspace documentation](https://here.now/docs#workspaces)
- [here.now access control documentation](https://here.now/docs#access-control)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, live URLs, and JSON-style status output from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May publish selected files to live URLs, create or update private Drive content, create scoped share tokens, and store credentials locally when the user authorizes authenticated use.]

## Skill Version(s):

1.19.0 (source: evidence.release.version and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
