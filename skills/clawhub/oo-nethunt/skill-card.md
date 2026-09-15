## Description:

NetHunt (nethunt.com). Use this skill for NetHunt requests, including reading, creating, updating, and deleting CRM data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate NetHunt CRM records, folders, fields, comments, call logs, and changes through a connected OOMOL account while relying on schema inspection before action execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could run installer scripts directly.

Mitigation: Install the oo CLI through a verified method before first use rather than letting an agent automatically run curl|bash or irm|iex.

Risk: Write and destructive NetHunt actions can create, update, or delete CRM records.

Mitigation: Require explicit user confirmation of the exact payload, target record, and expected effect before running create, update, or delete actions.

Risk: The skill operates through OOMOL-mediated server-side credentials.

Mitigation: Use only when the user accepts OOMOL mediation for NetHunt actions and has connected the intended account.

## Reference(s):

- [NetHunt homepage](https://nethunt.com)
- [ClawHub NetHunt skill page](https://clawhub.ai/oomol/skills/oo-nethunt)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector actions that return JSON responses when used by an agent.]

## Skill Version(s):

1.0.2 (source: evidence.json metadata and release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
