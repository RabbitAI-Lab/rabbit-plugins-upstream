## Description:

NinjaPear lets agents search and read company intelligence through the OOMOL-connected NinjaPear connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect NinjaPear action schemas, run company research actions, check email provider status, and view the authenticated account's credit balance through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute changing code on the user's machine.

Mitigation: Review the oo CLI installation source first, prefer an official signed or package-manager install path when available, and do not run pipe-to-shell installers from an elevated shell.

Risk: Running NinjaPear actions uses the user's OOMOL-connected NinjaPear account and can consume NinjaPear credits.

Mitigation: Treat account and billing actions as user-visible operations, check credit balance when cost is a concern, and stop on HTTP 402 or OOMOL_INSUFFICIENT_CREDIT until the user recharges.

## Reference(s):

- [ClawHub NinjaPear Skill Page](https://clawhub.ai/oomol/skills/oo-ninjapear)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [NinjaPear homepage](https://nubela.co/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live NinjaPear action schema before submitting JSON payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
