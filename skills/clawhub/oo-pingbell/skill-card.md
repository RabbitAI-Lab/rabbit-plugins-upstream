## Description:

PingBell enables agents to list PingBell sources and ring a selected source through an OOMOL-connected PingBell account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PingBell from an agent workflow, including listing sources and ringing a selected source after confirming the intended target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented installer uses a remote script execution pattern for the oo CLI.

Mitigation: Verify the oo CLI installer or use a safer package or release channel before installation.

Risk: The ring_source action changes PingBell state by updating counters, screens, and subscribed devices.

Mitigation: Require explicit user confirmation of the source and intended effect before running ring_source.

## Reference(s):

- [ClawHub PingBell Skill Page](https://clawhub.ai/oomol/skills/oo-pingbell)
- [PingBell Homepage](https://pingbell.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should use the live connector schema before constructing payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
