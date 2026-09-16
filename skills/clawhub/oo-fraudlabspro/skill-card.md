## Description:

FraudLabs Pro helps agents operate FraudLabs Pro through OOMOL's oo CLI to screen orders, retrieve screening results, and submit approve or reject feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to run FraudLabs Pro account workflows through an agent, including order screening, result retrieval, and approve or reject feedback. The skill is intended for connected OOMOL accounts with FraudLabs Pro configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Prefer a verified, reviewed, or package-managed installation path before running installer scripts.

Risk: FraudLabs Pro actions can change account state by screening orders or submitting approve or reject feedback.

Mitigation: Confirm the exact action, payload, and expected effect with the user before executing state-changing commands.

## Reference(s):

- [FraudLabs Pro homepage](https://www.fraudlabspro.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fraudlabspro)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector commands that return JSON responses from FraudLabs Pro.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
