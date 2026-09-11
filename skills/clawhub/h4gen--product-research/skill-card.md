## Description:

Identifies e-commerce product opportunities by correlating social trend signals, regional demand context, marketplace checks, sourcing options, and store draft preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[h4gen](https://clawhub.ai/user/h4gen)

### License/Terms of Use:


## Use Case:

E-commerce operators and developers use this skill to scout dropshipping or white-label product ideas, validate demand and competition signals, and prepare WooCommerce or Shopify-oriented store draft outputs. It is intended for evidence-backed product research and execution handoff, not profitability guarantees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance uses unpinned latest tooling and broad skill updates, which can install newer dependencies than the reviewed release used.

Mitigation: Review and pin the ClawHub CLI and dependency versions before installation, and avoid broad update commands unless the updated skills are reviewed.

Risk: WooCommerce or Shopify actions can affect a live store if connected production credentials are used.

Mitigation: Run setup from a least-privileged environment without production API keys, and confirm a staging or draft-only path before store operations.

## Reference(s):

- [Product Research ClawHub Skill Page](https://clawhub.ai/h4gen/skills/product-research)
- [Publisher Profile](https://clawhub.ai/user/h4gen)
- [ClawHub](https://clawhub.ai)
- [Inspected Upstream Skills](artifact/references/inspected-skills.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured sections and optional JSON-like store draft payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return partial results with MissingAPIKeys, DataGateStatus, or blocked deployment status when credentials or integrations are unavailable.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
