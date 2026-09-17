## Description:

Wangdian ERP support for searching and reading ERP records through the OOMOL-connected Wangdian connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to inspect Wangdian ERP records such as goods, inventory, orders, refunds, stockouts, shops, and warehouses through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes inline remote installer commands.

Mitigation: Use official, verifiable installation steps and checksums or signed packages before installing the oo CLI.

Risk: Wangdian ERP request parameters and returned business records pass through OOMOL.

Mitigation: Use only with an approved OOMOL account and confirm the user is comfortable routing this ERP data through the connector.

Risk: Authentication, connection, and billing setup can affect external accounts.

Mitigation: Run login or connection setup only after an explicit auth, scope, credential, app, or billing failure and with user approval.

## Reference(s):

- [Wangdian ERP homepage](https://www.wangdian.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wangdian)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect live connector schemas before constructing request payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
