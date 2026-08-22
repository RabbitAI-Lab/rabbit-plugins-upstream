## Description:

Provides a config-driven PromoStandards SOAP client for supplier inventory, product data, pricing, configuration, and purchase-order workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and integration agents use this skill to query promotional-products supplier capabilities, inventory, product details, pricing, decoration options, and purchase-order flows through PromoStandards services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier credentials can authorize live supplier data access or purchasing actions if bound too broadly.

Mitigation: Bind only the documented PS_<SUPPLIER>_ID and PS_<SUPPLIER>_PASSWORD credentials for intended suppliers and treat both values as secrets.

Risk: The send-po action can create a real purchase order when production mode is explicitly allowed.

Mitigation: Use preview-po before submission, require allowProduction for production orders, and escalate ambiguous purchase-order failures before retrying.

Risk: Generated supplier overrides can direct requests to incorrect endpoints if the registry or override data is wrong.

Mitigation: Review generated supplier overrides before committing them and validate supplier behavior with the bundled read-only smoke test where applicable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zmtucker/skills/promostandards)
- [PromoStandards](https://promostandards.org)
- [Config shape, adding a supplier, adding a version](references/adding_a_supplier.md)
- [PromoStandards registry findings](references/registry_findings.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON command output and concise Markdown guidance with inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads JSON payloads from stdin and uses environment-bound supplier credentials rather than accepting secrets in payloads.]

## Skill Version(s):

0.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
