## Description:

Booqable supports searching and reading company, customer, order, and product group data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Booqable business data, including customers, orders, product groups, and the connected company, through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose Booqable customer, order, company, and product data to the agent session.

Mitigation: Install and use it only for accounts where agent access to this business data is intended, and review sensitive results before sharing them outside the session.

Risk: First-time setup may involve a remote oo CLI installer command.

Mitigation: Review the oo CLI installation source before running the installer and avoid repeating setup commands unless an authentication or connection failure requires them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-booqable)
- [Booqable homepage](https://www.booqable.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
