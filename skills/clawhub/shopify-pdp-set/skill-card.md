## Description:

Turn seller-supplied product facts into one Shopify product-page stills set for a single SKU.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill to turn confirmed product facts for one SKU into a planned and generated set of Shopify product-page stills, with one still per named theme.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra device token covers broad media and task capabilities beyond still-image generation.

Mitigation: Install only in environments where that shared account access is acceptable, keep the token in the documented credential file, and revoke or reconnect access when the account or environment changes.

Risk: Silent self-updates are enabled by default and can replace package-owned files.

Mitigation: Use the documented update controls to disable automatic checks when package self-modification is not allowed, and rely on the package's verification and rollback behavior before continuing work.

Risk: Billable image generation can consume credits and asynchronous retries can duplicate work if request identity changes.

Mitigation: Confirm live pricing before paid calls, use one opaque client_request_id per unchanged request, and retry uncertain submissions only with byte-identical arguments.

## Reference(s):

- [Shopify PDP still workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell and JSON examples; generated still-image files and task metadata are returned by the Beatra task service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 4 to 8 stills for one SKU by default; billable generation uses one request per theme and reports task IDs, dimensions, formats, resolved models, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
