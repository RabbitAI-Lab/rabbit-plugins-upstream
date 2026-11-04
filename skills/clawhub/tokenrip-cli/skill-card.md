## Description:

Provides the `rip` CLI for shared Tokenrip workspaces, including artifact and table publishing, task workflows, reviews, stored API connections, and site deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[silostack](https://clawhub.ai/user/silostack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use the skill to collaborate in Tokenrip workspaces: retrieve project context, publish and organize shared artifacts, handle tasks and reviews, and use stored connections or deploy sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports conflicting workspace-deletion guidance and an example that weakens approval controls.

Mitigation: Resolve the conflicting guidance before unattended use, require approval for a specifically identified workspace deletion, use restricted connections, and review and pin installation sources.

## Reference(s):

- [Tokenrip](https://tokenrip.com)
- [Tokenrip CLI on ClawHub](https://clawhub.ai/silostack/skills/tokenrip-cli)
- [workspaces.md](references/workspaces.md)
- [tasks.md](references/tasks.md)
- [skills.md](references/skills.md)
- [connections.md](references/connections.md)
- [setup-and-identity.md](references/setup-and-identity.md)
- [output-and-provenance.md](references/output-and-provenance.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Code, CSV, HTML, JSON, Tables]

**Output Format:** [Markdown guidance with shell command examples; published artifacts use the requested format.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can publish workspace artifacts, update tables and tasks, call stored connections, and deploy static sites.]

## Skill Version(s):

2.6.16 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
