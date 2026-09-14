## Description:

Turn seller-supplied nutrition facts into one nutrition panel still per SKU. This nutrition panel art studio lays out the seller-supplied serving and nutrient lines as a nutrition facts label and nutrition panel graphic. Use it for food nutrition labels, packaging nutrition art, and product-page nutrition charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to produce SKU-level nutrition panel stills from nutrition facts they already supplied for packaging or product listing artwork.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account authority that can cover billable media operations and wallet-related access.

Mitigation: Install only when the publisher is trusted for that account authority, keep the device token private, and review the requested connection before use.

Risk: The bundled client can silently update package-owned code before ordinary commands.

Mitigation: Review the automatic update behavior and disable it with the documented update control when that is required for the deployment.

Risk: Selected local files may be uploaded as visual references.

Mitigation: Upload only seller-approved files after inspection and use returned artifact identifiers rather than exposing local paths.

Risk: Generated small nutrition text may be incorrect or unreadable and is not a certified nutrition label.

Mitigation: Review visible printed lines against the confirmed nutrition table and treat unreadable or mismatched text as a correction item.

Risk: Image generation is billable and actual charges may differ from the initial estimate.

Mitigation: Read the live model card before paid work, confirm the cost card with the user, submit each SKU once with a unique request identity, and report returned net charged credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/nutrition-panel-art)
- [Nutrition-panel workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, image files, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one still per SKU, with task IDs, dimensions, formats, resolved models, and net charged credits when available.]

## Skill Version(s):

0.1.3 (source: evidence.release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
