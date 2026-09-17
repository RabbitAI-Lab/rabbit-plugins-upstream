## Description:

LiveAgent (liveagent.com). Use this skill for LiveAgent requests to read, create, and update data through the OOMOL oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support operators use this skill to inspect LiveAgent action schemas and manage contacts, tickets, departments, and contact groups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup section references remote installer scripts for the oo CLI.

Mitigation: Review or replace installer steps before use, and prefer a versioned, signed, or checksum-verified CLI installation source.

Risk: LiveAgent write actions can create or update contacts and tickets.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running create or update actions.

## Reference(s):

- [LiveAgent homepage](https://www.liveagent.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-liveagent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return LiveAgent data from oo connector responses, including data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
