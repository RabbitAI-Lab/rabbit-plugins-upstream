## Description:

Turn seller-supplied SKU specs into a set of listing-ready SKU comparison chart stills, with one still per named comparison axis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and commerce teams use this skill to convert confirmed SKU names and spec rows into product comparison chart stills for listings. It plans chart axes, confirms paid image work, submits Beatra generation tasks, and returns generated files with task and billing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broad Beatra account authority for a narrow SKU-chart task, including paid wallet use and media-generation scopes.

Mitigation: Install only when the user accepts those account permissions, monitor Beatra wallet and account activity, and confirm live pricing before any billable generation.

Risk: The bundled client uses a shared local Beatra device credential.

Mitigation: Keep the credential in the documented user-only Beatra files, never print or copy tokens into chat, logs, command arguments, environment variables, or other package directories, and use the uninstall script when disconnecting.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when silent updates are not acceptable, and review package changes before continued use.

Risk: Seller files and reference images may be uploaded to Beatra.

Mitigation: Upload only files the user intentionally wants sent to Beatra, inspect local files before upload, and use returned artifact IDs instead of exposing local paths.

Risk: Generated chart text can be wrong or hard to read.

Mitigation: Review every generated still against the seller-confirmed spec list and treat small generated type as a review item rather than a certified specification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/sku-comparison-chart)
- [SKU comparison workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON payloads, shell commands, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 4 to 8 still-image files by default, one image-generation task per approved comparison axis, plus task IDs, resolved models, dimensions, formats, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
