## Description:

国内电商全链路运营 helps agents evaluate Chinese e-commerce products, pricing, ads, conversion funnels, listing content, compliance, inventory, and Temu workflows with reference playbooks and Python calculators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[g305595965](https://clawhub.ai/user/g305595965)

### License/Terms of Use:

MIT

## Use Case:

External e-commerce operators and agents use this skill to score products, calculate pricing and ad break-even points, diagnose sales funnels, generate compliant listing titles, plan inventory, and route current market inputs into calculators for China-focused marketplace operations.

### Deployment Geography for Use:

China-focused marketplace operations, with Temu cross-border workflows

## Known Risks and Mitigations:

Risk: The live-data helper can place values from live_data.json into shell commands that users or agents are instructed to execute.

Mitigation: Review live_data.json before running generated commands; use numeric or allowlisted values and prefer manual argument entry or quoted, validated command construction.

Risk: Marketplace fee, rule, conversion, and return-rate assumptions can become stale or differ by category.

Mitigation: Verify operational inputs against current merchant-backend or official public sources before using calculator results for business decisions.

Risk: Compliance checks are risk-screening guidance and may not resolve legal or regulated-claims edge cases.

Mitigation: Clear P0 advertising-law hits before publication and use qualified review for regulated categories or high-risk claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/g305595965/skills/cn-ecommerce-ops)
- [Skill instructions](artifact/SKILL.md)
- [README](artifact/README.md)
- [Platform playbook](artifact/references/platform-playbook.md)
- [Product selection](artifact/references/product-selection.md)
- [Listing and content](artifact/references/listing-and-content.md)
- [Operations playbook](artifact/references/operations-playbook.md)
- [Temu cross-border playbook](artifact/references/crossborder-temu.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-capable calculator output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Python standard-library scripts; generated live-data command plans should be reviewed before execution.]

## Skill Version(s):

1.2.1 (source: server evidence release.version, artifact/SKILL.md frontmatter, artifact/README.md changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
