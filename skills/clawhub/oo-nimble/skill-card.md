## Description:

Nimble lets an agent read, create, list, search, and update Nimble CRM contacts through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to manage Nimble CRM contacts through an OOMOL-connected account. It supports reading contact data and, after user confirmation, creating or updating contact records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that require manual trust review.

Mitigation: Prefer a verified package or reviewed installer before running the documented installer commands.

Risk: Create and update actions can change Nimble contact data.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: Nimble contact actions are routed through OOMOL's connector workflow.

Mitigation: Install only when the user trusts OOMOL with the connected Nimble workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-nimble)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Nimble Homepage](https://www.nimble.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
