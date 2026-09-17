## Description:

Fellow enables agents to read and update Fellow users, meeting notes, and action items through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to retrieve Fellow users, meeting notes, and action items, and to carry out confirmed action-item updates such as completion or archiving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute changing code on a user's machine.

Mitigation: Prefer an official, versioned installation method with checksum or signature verification, and review installer content before running it.

Risk: The skill uses OOMOL-mediated access to the user's Fellow account.

Mitigation: Install only when that access model is acceptable, and keep the connected Fellow account scoped to the intended workspace and use.

Risk: Write actions can modify Fellow action items.

Mitigation: Fetch the live connector schema, review the exact payload and expected effect, and obtain user confirmation before executing write actions.

## Reference(s):

- [ClawHub Fellow skill page](https://clawhub.ai/oomol/skills/oo-fellow)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Fellow homepage](https://fellow.app)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit oo CLI commands and JSON connector payloads; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
