## Description:

Oomnitza helps agents search and read Oomnitza asset and user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and IT operations teams use this skill to inspect Oomnitza assets, users, and connection metadata through an OOMOL-connected account. It supports read-only listing and retrieval workflows and instructs agents to inspect the live connector schema before running an action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path asks users to run an internet installer directly in a shell.

Mitigation: Use a verified or separately reviewed oo CLI installation method before enabling the skill.

Risk: The skill reads Oomnitza assets and users through OOMOL-mediated access.

Mitigation: Confirm the connected Oomnitza account is scoped only to the asset and user data the agent should read.

Risk: Connector action payloads can drift from examples or assumptions.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-oomnitza)
- [Oomnitza homepage](https://www.oomnitza.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Oomnitza connector results returned as JSON under data and execution metadata under meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
