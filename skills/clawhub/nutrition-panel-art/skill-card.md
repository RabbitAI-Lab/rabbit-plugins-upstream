## Description:

Turn seller-supplied nutrition facts into one nutrition panel still per SKU.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to turn their confirmed nutrition tables into labeled nutrition-panel stills for named SKUs. It plans the card list first, then generates one image per approved SKU through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra credential grants broader account authority than nutrition-panel image generation alone.

Mitigation: Review requested access before installation, keep the device token private, and revoke the connected agent from the Beatra Console when the skill is no longer needed.

Risk: Approved generation and edit tasks can spend Beatra credits.

Mitigation: Read live model pricing before billable calls, show the user the work, credits, count, request identity, stop condition, and balance recovery path, and submit each approved SKU once with an opaque client_request_id.

Risk: The bundled client can silently install package updates by default.

Mitigation: Use the documented update controls to disable automatic checks when required, and rely on the package's checksum, archive, manifest, rollback, and fixed-source verification before accepting updates.

Risk: Generated nutrition-panel small type may be incorrect or unreadable.

Mitigation: Use only seller-confirmed nutrition facts, review visible printed text against the confirmed table, and treat the result as product artwork rather than a certified legal nutrition label.

## Reference(s):

- [Nutrition-panel workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/nutrition-panel-art)
- [Beatra skill homepage](https://beatra.ai/skills/nutrition-panel-art)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured task cards, JSON payload examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled plan plus generated image files, task IDs, observed dimensions and formats, resolved models, and net charged credits after approved Beatra tasks complete.]

## Skill Version(s):

0.1.1 (source: manifest.json and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
