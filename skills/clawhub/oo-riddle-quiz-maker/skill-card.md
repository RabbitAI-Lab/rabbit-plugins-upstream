## Description:

Operate Riddle Quiz Maker through an OOMOL-connected account to read, publish, rename, tag, and unpublish Riddle content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Riddle Quiz Maker projects and Riddles through the OOMOL oo CLI, including retrieval, publishing, embed-code lookup, renaming, and tag management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remotely downloaded installer scripts without integrity verification.

Mitigation: Install the oo CLI out of band from official documentation, review the installer before use, and avoid executing downloaded installer scripts blindly.

Risk: The skill can publish, rename, tag, remove tags from, or unpublish Riddle content.

Mitigation: Require explicit user confirmation for publish, rename, tag removal, unpublish, and other write actions, including the exact target and payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-riddle-quiz-maker)
- [Riddle Quiz Maker homepage](https://www.riddle.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect live connector schemas before action execution and require confirmation before write or destructive operations.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
