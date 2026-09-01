## Description:

Xero connector skill for reading, creating, and updating Xero data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Xero connector schemas, read accounting data, and create or update supported Xero records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access financial data in Xero through an OOMOL-connected account.

Mitigation: Install only when the agent is expected to access Xero data through OOMOL, and keep account connection scope aligned with the intended work.

Risk: Write actions can create contacts, create draft invoices, or update invoice status.

Mitigation: Confirm the exact payload and intended effect with the user before executing any write action.

Risk: Connector schemas can change over time and stale payload assumptions may cause incorrect requests.

Mitigation: Inspect the live action schema with the oo CLI before constructing each action payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-xero)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Xero homepage](https://www.xero.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke Xero connector actions through the oo CLI after inspecting live action schemas.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
