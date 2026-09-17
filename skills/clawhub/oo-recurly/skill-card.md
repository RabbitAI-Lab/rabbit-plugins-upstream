## Description:

Operate Recurly through an OOMOL-connected account with the oo CLI to read, create, and update account, plan, and subscription data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operations teams use this skill to inspect and manage Recurly accounts, plans, and subscriptions through an OOMOL-connected account. It supports schema-first read actions and controlled write workflows for creating accounts, plans, and subscriptions, plus updating account profile fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer path before use and prefer a verified, pinned, or signed oo CLI distribution method.

Risk: Several Recurly actions create or update accounts, plans, and subscriptions.

Mitigation: Approve write actions only after checking the exact JSON payload and expected business effect.

## Reference(s):

- [ClawHub Recurly Skill](https://clawhub.ai/oomol/skills/oo-recurly)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Recurly Homepage](https://recurly.com)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation of payload and effect.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
