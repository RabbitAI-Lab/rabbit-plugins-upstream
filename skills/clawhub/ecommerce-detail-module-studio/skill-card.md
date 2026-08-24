## Description:

Turns confirmed SKU facts and product photos into three to six coordinated ecommerce detail modules with a visual story and layout handoff for Amazon A+ Content, product detail pages, brand storefronts, Shopify product pages, and launch campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and page builders use this skill to turn approved SKU facts and product photos into three to six product-detail or A+ Content modules plus a layout handoff. It helps plan module sequence, confirm facts and paid image-generation work, run Beatra image tasks, and deliver accepted artifacts with placement notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device authorization and can upload product assets to Beatra.

Mitigation: Install only when that account access and product-asset upload are acceptable; avoid sensitive product or business content unless the authorization has been reviewed.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates with the documented update command when review-before-update is required.

Risk: Beatra generation tasks consume credits and changed retries can create new paid work.

Mitigation: Confirm the module set and maximum price before execution, keep one client_request_id per module, and retry only unchanged requests with the same identity after uncertain transport failures.

Risk: The package performs non-billable registration telemetry for package slug, version, platform, and installation reference.

Mitigation: Install only if this package registration telemetry is acceptable for the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ecommerce-detail-module-studio)
- [Beatra skill homepage](https://beatra.ai/skills/ecommerce-detail-module-studio)
- [Detail-module workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown handoff with shell command examples and JSON MCP payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image artifact references, task IDs, resolved models, observed output details, and Beatra billing fields when remote tasks succeed.]

## Skill Version(s):

0.1.3 (source: evidence release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
