## Description:

PingBell (pingbell.io). Use this skill for ANY PingBell request - searching and reading data. Whenever a task involves PingBell, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PingBell through an OOMOL-connected account, including listing available sources and ringing a selected source after confirming the intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ring a PingBell source, which updates its counter, screens, and subscribed devices through the connected account.

Mitigation: Require explicit confirmation of the target source and expected effect before running the ring_source action.

Risk: The security summary reports a mismatch between read-oriented wording and an available state-changing ring action.

Mitigation: Treat ring_source as state-changing even if it is not tagged in the action list, and review the connector schema before execution.

Risk: Commands use connected account credentials managed by OOMOL.

Mitigation: Use the skill only where the connected account is appropriate for the requested PingBell operation.

## Reference(s):

- [PingBell Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-pingbell)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [PingBell Homepage](https://pingbell.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live PingBell connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
