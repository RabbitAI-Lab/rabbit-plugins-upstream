## Description:

Compares a primary ASIN with authorized competitor product-page fields, images, and review evidence to identify Listing expression gaps and verifiable improvements, without assessing real-time price, sales, inventory, advertising, orders, or true return rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and listing operators use this skill to compare a primary ASIN with an authorized competitor listing, identify evidence-backed Listing gaps, and generate improvement recommendations after ARI account checks and quote/confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad ARI account-linked operations beyond the narrow Listing-gap workflow.

Mitigation: Install only when broad ARI account access is intended, and keep use scoped to the fixed page_compare/listing_gap workflow unless the user explicitly requests other ARI operations.

Risk: Billable collection, analysis, and account auto-confirm behavior can consume ARI credits.

Mitigation: Review or disable auto-confirm settings, use quote-only flows for pricing questions, and require explicit confirmation before operations that return confirmationRequired.

Risk: Custom ARI endpoint settings could redirect account API traffic if intentionally enabled.

Mitigation: Use the official ARI endpoint unless operating a controlled environment, and avoid custom ARI_BASE_URL settings unless the endpoint is trusted.

Risk: Local exports can write report or review data to disk.

Mitigation: Create exports only when requested, store them in approved local paths, and review generated files before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-listing-gap)
- [Operation workflow](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)
- [User guide](使用说明.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown reports and concise operational guidance with optional shell commands, structured JSON command responses, report links, and local exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN/site scope, sample counts, report IDs, credit usage, account-status notes, and links to ARI-hosted reports when returned by the service.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
