## Description:

Creates AI product-on-model images and clothing try-on presentations from apparel and wearable-accessory product photos for localized ecommerce campaigns, with one market-specific fashion-model visual planned per sales market.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and marketing teams use this skill to turn confirmed apparel and wearable-accessory SKU photos into localized on-model visuals for fashion listings, storefronts, ads, and social commerce campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared broad Device Token for Beatra access.

Mitigation: Review the requested account access before installation, keep the token only in the documented local credential file, and reconnect only when the user explicitly chooses to do so.

Risk: Automatic self-updates are enabled by default.

Mitigation: In managed or sensitive environments, disable automatic updates with `python3 scripts/mcp_client.py update --auto off` before normal use and rely on reviewed updates.

Risk: Billable generation requests can create duplicate charges if retried with changed inputs or new request identifiers.

Mitigation: Freeze the approved market set, use one stable `client_request_id` per market, and retry only the identical payload when delivery is uncertain.

Risk: Generated images may visibly drift from protected SKU details or market direction.

Mitigation: Compare accessible results against the recorded must-keeps, product readability, pose, styling, scene, and destination fit before delivery.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/product-on-model-locale-studio)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/product-on-model-locale-studio)
- [Market visual workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one count: 1 image-generation request per approved market and reports task, artifact, model, dimension, format, and billing details returned by Beatra.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
