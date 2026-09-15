## Description:

Browse AI (browse.ai). Use this skill for ANY Browse AI request: reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to inspect Browse AI action schemas, list and inspect robots and tasks, run robot tasks, and update robot cookies through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may execute unverified remote installer scripts.

Mitigation: Review or verify the oo CLI installer through a trusted source before running one-line remote install commands.

Risk: Browse AI account state can change when starting robot tasks or updating robot cookies.

Mitigation: Require explicit user approval for actions that start robot tasks, update cookies, or otherwise affect the Browse AI account.

## Reference(s):

- [Browse AI homepage](https://www.browse.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; state-changing actions require explicit confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
