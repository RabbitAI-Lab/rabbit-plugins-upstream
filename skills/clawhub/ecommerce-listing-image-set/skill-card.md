## Description:

Turn verified SKU facts and product photos into AI product listing images: a coordinated ecommerce image set for Amazon listing images, Shopify product images, Etsy listing photos, and online marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and marketplace teams use this skill to plan and generate a cohesive image gallery for one verified SKU, including hero, feature, detail, lifestyle, size or fit, and packaging or in-box views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra media-generation and account capabilities through a shared persistent device credential.

Mitigation: Install only when that credential model is acceptable, review Beatra account activity, and revoke the device from the Beatra Console when no longer needed.

Risk: The bundled client can silently replace package-owned files through automatic updates.

Mitigation: Use the documented `python3 scripts/mcp_client.py update --auto off` command before routine use if silent updates are not acceptable.

## Reference(s):

- [Listing-set workflow](references/workflow.md)
- [A complete listing set, start to finish](references/worked-example.md)
- [Listing-set questions and anti-patterns](references/faq.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, image artifacts]

**Output Format:** [Markdown guidance with JSON request examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ordered slot plans, approved fact sources, task IDs, generated image artifacts, resolved models, and billing details when available.]

## Skill Version(s):

0.1.9 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
