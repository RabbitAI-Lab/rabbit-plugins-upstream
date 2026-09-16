## Description:

Ozon (ozon.ru). Use this skill for ANY Ozon request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and seller-operations users use this skill to read Ozon seller account information, product catalog data, product details, prices, stock quantities, and FBS or rFBS posting data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that are not independently verified in the evidence.

Mitigation: Prefer official, versioned installer documentation with checksum or signature verification, and avoid running installer commands unless setup is actually required.

Risk: Trigger wording is broader than the authenticated Ozon seller-account read use case.

Mitigation: Use the skill only for explicit seller-account data requests and fetch the live connector schema before each action payload.

## Reference(s):

- [Ozon homepage](https://www.ozon.ru)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Ozon connection settings](https://console.oomol.com/app-connections?provider=ozon)

## Skill Output:

**Output Type(s):** [Shell commands, JSON payloads, Configuration guidance, Markdown guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.]

## Skill Version(s):

1.0.2 (source: evidence metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
