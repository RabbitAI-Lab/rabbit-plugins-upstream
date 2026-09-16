## Description:

Shopify Partner helps an agent inspect and operate Shopify Partner data through an OOMOL-connected account using the shopify_partner connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Shopify Partner connector actions, including GraphQL queries, app lookup, Partner event retrieval, and earnings transaction listing through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is framed around reading data but exposes execute_graphql, which can run Shopify Partner mutations.

Mitigation: Manually review every execute_graphql payload and treat GraphQL mutations as write operations requiring explicit user confirmation before execution.

Risk: First-time setup includes remote script installation for the oo CLI.

Mitigation: Prefer verified or package-manager installation of the oo CLI instead of piping remote scripts directly into a shell.

Risk: The skill accesses Shopify Partner data through an OOMOL-connected account.

Mitigation: Install and use it only when the operator is comfortable connecting OOMOL to Shopify Partner data and has appropriate account authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shopify-partner)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Shopify Partner homepage](https://www.shopify.com/partners)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when commands are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
