## Description:

Tick (tickspot.com). Use this skill for Tick requests involving reading, creating, updating, and deleting data through the OOMOL-connected Tick connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Tick time-tracking data through an OOMOL-connected account. It supports listing and retrieving Tick records as well as creating, updating, and deleting time entries with user confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote script execution.

Mitigation: Review OOMOL's CLI installation method before installing and prefer a verified installer or documented manual install path.

Risk: The skill can create, update, or delete Tick time entries.

Mitigation: Require explicit user confirmation before running write or destructive Tick actions, including confirmation of the exact payload and intended effect.

Risk: Tick access is mediated through OOMOL-connected account credentials.

Mitigation: Use the skill only when the user is comfortable letting OOMOL mediate Tick access.

## Reference(s):

- [Tick homepage](https://www.tickspot.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tick)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
