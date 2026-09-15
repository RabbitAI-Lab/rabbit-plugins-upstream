## Description:

GenPage lets agents read and manage GenPage workspaces, campaigns, audiences, leads, variables, analytics, and account credits through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage GenPage resources through an OOMOL-connected account, including listing workspaces, campaigns, audiences, variables, analytics, and credit balances. It can also create or link campaigns and audiences when the user confirms the intended changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes mutable remote installer commands for the oo CLI.

Mitigation: Install the oo CLI manually from trusted OOMOL instructions and verify installer commands before connecting an account.

Risk: The skill can run write or destructive GenPage actions through an authenticated connector.

Mitigation: Confirm exact payloads and targets before write actions, and require explicit approval before delete, remove, or unlink operations.

## Reference(s):

- [GenPage on ClawHub](https://clawhub.ai/oomol/skills/oo-genpage)
- [GenPage homepage](https://www.genpage.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON payloads, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are run through the oo CLI against the GenPage connector; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
