## Description:

Booqable (booqable.com) supports reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Booqable action schemas and run company, customer, order, and product-group actions through an OOMOL-connected account. It supports read, search, and listed state-changing workflows with confirmation guidance for actions that may modify or expose business data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified remote installer for the oo CLI.

Mitigation: Review the setup path before installing, prefer a verified package or signed release, and do not let an agent run the remote installer automatically.

Risk: Booqable actions can expose customer, order, company, and product data, and at least one action is documented with a write/read inconsistency.

Mitigation: Confirm any operation that could create, update, or expose customer or order data, and inspect the live action schema before constructing requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-booqable)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Booqable homepage](https://www.booqable.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing oo CLI requests; responses are JSON objects with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
