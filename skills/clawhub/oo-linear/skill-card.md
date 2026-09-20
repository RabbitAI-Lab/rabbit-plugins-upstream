## Description:

Linear (linear.app). Use this skill for ANY Linear request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read and manage Linear issues, projects, teams, comments, labels, attachments, milestones, reactions, cycles, states, users, and related workflow data through an OOMOL-connected Linear account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad state-changing Linear actions, including write and destructive operations.

Mitigation: Require the agent to show the exact payload and expected effect before approving write or destructive Linear actions.

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer verified or package-manager installation for the oo CLI when available, and run remote installers only after reviewing the source and trusting OOMOL.

## Reference(s):

- [Linear homepage](https://linear.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect connector schemas and run Linear actions with JSON input and output.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
