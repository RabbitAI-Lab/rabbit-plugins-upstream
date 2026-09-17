## Description:

Float (float.com) lets an agent search and read Float workspace data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list Float accounts, allocations, clients, people, and projects through an OOMOL-connected Float account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review installation steps manually and prefer a pinned, verifiable oo CLI release or package manager; do not allow an agent to run remote installers automatically.

Risk: Read-oriented Float actions may expose sensitive scheduling and business data.

Mitigation: Run only the actions needed for the user request and avoid sharing returned Float data beyond the intended audience.

## Reference(s):

- [Float homepage](https://www.float.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-float)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON responses with data and meta.executionId when actions execute.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
