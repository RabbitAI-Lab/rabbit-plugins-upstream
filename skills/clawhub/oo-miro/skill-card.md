## Description:

Operate Miro through an OOMOL-connected account to read, create, and update boards and board items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Miro boards through the oo CLI with their connected OOMOL/Miro account. It supports listing and retrieving boards and items, plus creating boards, sticky notes, and text items after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create Miro boards, sticky notes, and text items using the connected account.

Mitigation: Confirm the exact action, target board, and JSON payload before approving any write action.

Risk: The first-time setup path can install the third-party oo CLI.

Mitigation: Treat CLI installation as a normal third-party command-line install and review the installer before running it.

Risk: The skill operates through the user's connected OOMOL/Miro account.

Mitigation: Install and use it only when agent access to that connected account is intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-miro)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Miro](https://miro.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON payloads, guidance]

**Output Format:** [Markdown with bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
