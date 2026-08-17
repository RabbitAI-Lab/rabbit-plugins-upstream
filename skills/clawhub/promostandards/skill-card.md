## Description:

Config-driven PromoStandards client for suppliers that publish standard SOAP services, covering inventory, product data, pricing and configuration, and purchase-order workflows through per-supplier configuration and per-version adapters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and procurement-focused agents use this skill to query supplier capabilities, inventory, product data, pricing, decoration information, and purchase-order flows for PromoStandards suppliers. Operators can provision supplier configuration from the public registry and keep credentials in environment bindings instead of config files or prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier credentials may be exposed or misused if they are placed in prompts, stdin payloads, or committed configuration files.

Mitigation: Use only environment-bound credentials named for the selected supplier and review credential bindings before installing in environments with real supplier accounts.

Risk: Untrusted callers or prompt content could supply arbitrary configJson endpoint URLs and redirect supplier requests.

Mitigation: Allow only trusted, registry-generated supplier configurations and reject or review inline endpoint configuration from untrusted sources.

Risk: Production purchase-order submission can affect real orders and may create duplicate or incorrect orders if enabled too broadly.

Mitigation: Require an explicit boolean production approval path before using send-po with production credentials, and prefer preview-po or test endpoints for review.

## Reference(s):

- [PromoStandards](https://promostandards.org)
- [Registry findings](references/registry_findings.md)
- [Adding a supplier](references/adding_a_supplier.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [JSON objects, Markdown guidance, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supplier actions read JSON input and print one JSON object to stdout; supplier configs use environment-variable credential references.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
