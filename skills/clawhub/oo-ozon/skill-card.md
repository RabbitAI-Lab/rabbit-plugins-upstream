## Description:

Ozon (ozon.ru) helps agents search and read Ozon seller account, product, price, stock, and FBS/rFBS posting data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and marketplace users use this skill to let an agent read Ozon seller account, catalog, pricing, stock, and FBS/rFBS posting data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions tell users or agents to run remote installer scripts directly, which could execute unverified code.

Mitigation: Use the Ozon read actions only after the oo CLI is already installed from a trusted, verified source; inspect installers or use official signed/package-manager installation instructions when available.

## Reference(s):

- [Ozon homepage](https://www.ozon.ru)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-ozon)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
