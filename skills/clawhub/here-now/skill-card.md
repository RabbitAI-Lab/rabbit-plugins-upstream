## Description:

here.now lets agents publish websites and files to live URLs, manage hosted Site access, use private Drive storage, and buy domains for Sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to publish generated websites and files, update or protect hosted Sites, work with private Drive storage, and register custom domains through here.now workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist a long-lived API key and project-local site claim tokens.

Mitigation: Install only if the publisher is trusted, keep credential files permission-restricted, and keep local state files out of source control.

Risk: Drive export has a reviewed risk around unsafe file writes for untrusted or shared Drives.

Mitigation: Avoid Drive export on untrusted or shared Drives until path traversal protections are fixed, and prefer narrow scoped Drive tokens with short TTLs.

Risk: The recommended global npx installation can fetch changing package contents.

Mitigation: Use pinned or project-local installation when reproducibility or change control matters.

Risk: Publishing uploads selected files to here.now and storage upload endpoints and may expose content if access controls are not set correctly.

Mitigation: Review files before publishing and use password, restricted, or workspace access for private content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/adamludwin/skills/here-now)
- [here.now Docs](https://here.now/docs)
- [here.now OpenAPI Schema](https://here.now/openapi.json)
- [Buy Domain Docs](https://here.now/docs#buy-domain)
- [Workspace Docs](https://here.now/docs#workspaces)
- [Access Control Docs](https://here.now/docs#access-control)
- [Version History Docs](https://here.now/docs#versions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and live URL output from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local credential and state files, upload selected files, and call here.now APIs when used by an agent.]

## Skill Version(s):

1.29.0 (source: artifact/SKILL.md and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
