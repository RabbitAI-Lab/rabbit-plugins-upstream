## Description:

Mem (mem.ai). Use this skill for ANY Mem request - reading, creating, updating, and deleting data. Whenever a task involves Mem, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Mem notes through an OOMOL-connected account, including creating, reading, listing, searching, updating, trashing, restoring, and permanently deleting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include running a remote installer script on the user's machine.

Mitigation: Review the official oo CLI installation path before running installers, and do not let an agent execute curl-to-bash or PowerShell iex installers automatically.

Risk: The skill can create, overwrite, trash, restore, or permanently delete Mem notes.

Mitigation: Require explicit user confirmation for note creation, overwrite, trash, restore, and deletion, including the exact target and payload.

Risk: Mem access is mediated by OOMOL.

Mitigation: Install only when the user is comfortable using OOMOL as an intermediary for Mem access.

## Reference(s):

- [Mem homepage](https://mem.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mem)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: evidence release version and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
