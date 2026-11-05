## Description:

Use the Tokenrip `rip` CLI to manage shared workspaces, artifacts, tasks, reviews, stored connections, and deployments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silostack](https://clawhub.ai/user/silostack)

### License/Terms of Use:

MIT

## Use Case:

Developers and AI agents use `rip` to resume shared project work, manage workspace files and tasks, submit actions for review, and publish or share outputs through Tokenrip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace access can expose or change shared artifacts, publish public links, and call provider APIs through stored connections.

Mitigation: Grant only intended workspace and connection access, restrict endpoints and team access, review sharing, and use automatic approval only for work you trust.

Risk: The external CLI implementation and claimed server safeguards have not been verified.

Mitigation: Review proposed actions and outputs, and do not rely on unverified safeguards when deciding whether to approve sensitive work.

## Reference(s):

- [Tokenrip](https://tokenrip.com)
- [Tokenrip CLI skill release](https://clawhub.ai/silostack/skills/tokenrip-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Shell commands and workspace artifacts such as Markdown, HTML, code, CSV, JSON, and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the requested workspace task.]

## Skill Version(s):

2.6.18 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
