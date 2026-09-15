## Description:

Webvizio helps agents manage Webvizio REST Hook subscriptions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Webvizio connector action schemas and create or delete REST Hook subscriptions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute mutable remote installer scripts without independent verification.

Mitigation: Review and verify the OOMOL CLI installer before running it; prefer a trusted installation path when available.

Risk: The skill can create or delete Webvizio REST Hook subscriptions.

Mitigation: Inspect the live action schema and confirm the exact payload, target webhook, and expected effect before any write or destructive command.

Risk: The skill summary routes broad Webvizio requests to a narrow set of documented REST Hook actions.

Mitigation: Limit use to the documented connector actions unless live schema inspection confirms additional supported actions.

## Reference(s):

- [Webvizio homepage](https://webvizio.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-webvizio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
