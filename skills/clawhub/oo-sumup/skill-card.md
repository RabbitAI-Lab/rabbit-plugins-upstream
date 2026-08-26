## Description:

Operate SumUp through an OOMOL-connected account for checkout, customer, and payment-instrument workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect SumUp connector schemas and run SumUp actions through an OOMOL-connected account. It supports creating, retrieving, listing, updating, and deactivating SumUp checkout and customer records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform financial write and destructive actions in a connected SumUp account.

Mitigation: Review payloads and obtain explicit user approval before checkout creation, customer updates, or checkout deactivation.

Risk: Connector schemas and account connection state may affect accepted payloads or available actions.

Mitigation: Inspect the live oo connector schema before constructing payloads and use setup steps only after authentication or connection errors.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sumup)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [SumUp Homepage](https://www.sumup.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before action execution and returns connector responses as JSON.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
