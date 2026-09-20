## Description:

Get Biji (biji.com). Use this skill for reading, creating, updating, deleting, sharing, tagging, and searching Get Biji notes and knowledge bases through the OOMOL getnote connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate a connected Get Biji account for note, tag, knowledge base, blogger, and live-session workflows. It is intended for read, write, search, share, and destructive note-management tasks with user confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run a remote oo CLI installer script on the user's machine without independent verification.

Mitigation: Review the installer source before running setup commands, and use the setup path only after a command fails because the CLI is missing.

Risk: Write and destructive actions can alter Get Biji notes, tags, and knowledge bases.

Mitigation: Require clear user confirmation of the exact payload, target note, tag, or knowledge base before executing actions marked write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-getnote)
- [Get Biji Homepage](https://www.biji.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing instructions for inspecting live connector schemas and running oo CLI actions]

## Skill Version(s):

1.0.5 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
