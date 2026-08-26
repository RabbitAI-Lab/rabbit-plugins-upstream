## Description:

Miro (miro.com) helps agents read, create, and update Miro boards and items through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to inspect Miro boards and items and create boards, sticky notes, or text through an OOMOL-connected Miro account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create actions can change Miro state by adding boards, sticky notes, or text.

Mitigation: Confirm the exact action, target, and payload with the user before running write actions.

Risk: The skill accesses Miro through an OOMOL-connected account.

Mitigation: Install and use it only when that account-level connector access is acceptable for the workspace.

## Reference(s):

- [ClawHub Miro skill listing](https://clawhub.ai/oomol/skills/oo-miro)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Miro homepage](https://miro.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires checking each action's live connector schema before building payloads.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
