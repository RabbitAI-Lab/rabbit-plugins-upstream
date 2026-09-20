## Description:

Operates Healthchecks.io through an OOMOL-connected account using the oo CLI for reading, creating, updating, pausing, resuming, and deleting Healthchecks.io resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Healthchecks.io checks and project resources through an OOMOL-connected account. It supports status review, project listing, and confirmed lifecycle changes for checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts for the oo CLI.

Mitigation: Install only if OOMOL and the oo CLI distribution path are trusted; prefer a versioned or package-manager install path and inspect or verify installer contents before running them.

Risk: Write and destructive Healthchecks.io actions can create, update, pause, resume, or delete checks.

Mitigation: Require explicit approval for these actions and confirm the exact payload, target, and expected effect before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-healthchecks-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Healthchecks.io homepage](https://healthchecks.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence release and metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
