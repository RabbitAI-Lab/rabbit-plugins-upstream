## Description:

Payrexx lets agents operate a user's OOMOL-connected Payrexx account to read payment data and create hosted checkout gateways through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Payrexx gateways, transactions, and payment providers, and create hosted checkout gateways after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create Payrexx payment gateways and change account state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: A connected Payrexx account may have broader access than the task requires.

Mitigation: Use an OOMOL Payrexx connection with only the scopes needed for the intended actions.

Risk: Authentication, connection, or billing failures can interrupt connector actions.

Mitigation: Use the first-time setup and reconnection steps only after matching command failures occur.

## Reference(s):

- [ClawHub Payrexx skill page](https://clawhub.ai/oomol/skills/oo-payrexx)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Payrexx homepage](https://payrexx.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions run through the oo CLI return JSON data with meta.executionId.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
