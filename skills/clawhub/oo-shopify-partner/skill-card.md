## Description: <br>
Shopify Partner (shopify.com). Use this skill for ANY Shopify Partner request - searching and reading data. Whenever a task involves Shopify Partner, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to inspect Shopify Partner apps, app events, partner events, and earnings transactions, and to run Shopify Partner GraphQL operations through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes a broad Shopify Partner GraphQL interface that can run mutations even though its summary emphasizes searching and reading data. <br>
Mitigation: Require explicit user confirmation for every mutation, including the exact payload and expected effect, before execution. <br>
Risk: Broad or sensitive Shopify Partner tasks may have business impact if the query or mutation scope is unclear. <br>
Mitigation: Inspect the live action schema and review the GraphQL operation before routing sensitive tasks through the connector. <br>


## Reference(s): <br>
- [ClawHub Shopify Partner Skill](https://clawhub.ai/oomol/skills/oo-shopify-partner) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Shopify Partner Homepage](https://www.shopify.com/partners) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId; GraphQL mutations require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
