## Description:

Turn seller-supplied product facts into a Shopify product-page image set for a single SKU.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and their agents use this skill to plan and generate Shopify product-page still image sets from confirmed SKU facts. It is intended for Shopify detail pages, listing galleries, and product detail images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token can authorize capabilities beyond Shopify image generation and may allow credit-spending operations.

Mitigation: Use the skill only in environments where shared Beatra authorization and spend authority are acceptable; confirm live model pricing before billable calls and report returned net charged credits.

Risk: Automatic package updates are enabled by default and can replace package-owned executable files.

Mitigation: Review the automatic update behavior before installation and disable silent checks with the documented update command when a fixed reviewed package is required.

Risk: Generated product-page images can contain inaccurate or unsupported visible claims.

Mitigation: Use only seller-confirmed SKU facts in prompts and review visible text against the confirmed fact list before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/shopify-pdp-set)
- [Beatra skill homepage](https://beatra.ai/skills/shopify-pdp-set)
- [Shopify PDP still workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with JSON MCP payloads and generated image artifact files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one still per confirmed theme, normally 4 to 8 1:1 2K images for one SKU; completed tasks report artifacts, resolved model, usage, and net charged credits.]

## Skill Version(s):

0.1.3 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
