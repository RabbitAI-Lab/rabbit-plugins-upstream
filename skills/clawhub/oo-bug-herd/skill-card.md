## Description:

BugHerd (bugherd.com). Use this skill for ANY BugHerd request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate BugHerd through an OOMOL-connected account, including reading projects, tasks, comments, attachments, and organization details. With user confirmation for writes, it can create and update BugHerd projects, tasks, comments, and URL-based attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands for the oo CLI, which could execute unreviewed code if run blindly.

Mitigation: Use a trusted OOMOL distribution path and prefer a signed or checksum-verified installer before installing the CLI.

Risk: Write actions can create or update BugHerd projects, tasks, comments, and attachments.

Mitigation: Review the live action schema and confirm the exact payload and effect with the user before executing write actions.

## Reference(s):

- [BugHerd homepage](https://bugherd.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bug-herd)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
