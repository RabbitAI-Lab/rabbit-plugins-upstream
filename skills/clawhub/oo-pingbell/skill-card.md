## Description:

PingBell enables agents to list PingBell sources and ring a selected source through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PingBell from an OOMOL-connected account. It supports listing available PingBell sources and ringing a source so its counter, screens, and subscribed devices update.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance can execute remote installer scripts without verification.

Mitigation: Review the installer step before use and prefer official installation documentation or packages with checksum or signature verification.

Risk: The ring_source action changes PingBell state.

Mitigation: Confirm the exact source, payload, and expected effect with the user before running ring_source.

## Reference(s):

- [PingBell homepage](https://pingbell.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pingbell)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; ring_source is a write action that changes PingBell state.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
