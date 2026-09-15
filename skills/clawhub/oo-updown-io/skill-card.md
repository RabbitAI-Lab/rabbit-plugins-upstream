## Description:

Operate updown.io monitoring checks through the OOMOL-connected oo CLI, including read, create, update, and delete actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage updown.io monitoring checks and node information from an agent session. It supports routine reads as well as confirmed create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer one-liners could execute unverified code during first-time setup.

Mitigation: Install the oo CLI only through a trusted source and verification process; do not allow an agent to run the installer commands automatically.

Risk: Write and destructive connector actions can change or delete updown.io monitoring checks.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before create, update, or delete actions.

## Reference(s):

- [updown.io homepage](https://updown.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-updown-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
