## Description:

here.now lets agents publish websites and files to live here.now URLs, update access-controlled sites, and use private Drive storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to publish local files or folders to here.now URLs, update sites, configure access modes, and manage private Drive content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish selected files to live URLs and manage private Drive content.

Mitigation: Review folders for secrets before publishing and install only when this publishing and Drive authority is intended.

Risk: Saved here.now credentials can provide durable access.

Mitigation: Prefer scoped short-lived Drive tokens where possible, and remove or rotate ~/.herenow/credentials when durable access is no longer needed.

## Reference(s):

- [here.now docs](https://here.now/docs)
- [Site versions](https://here.now/docs#versions)
- [Workspaces](https://here.now/docs#workspaces)
- [Site access control](https://here.now/docs#access-control)
- [ClawHub skill page](https://clawhub.ai/adamludwin/skills/here-now)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, URLs, and status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update here.now Sites, Drive files, access settings, and local state when the bundled scripts are run.]

## Skill Version(s):

1.21.0 (source: evidence release and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
