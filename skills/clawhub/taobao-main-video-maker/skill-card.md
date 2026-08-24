## Description:

Create a Taobao product main-image video or Tmall product main-image video from product photos, selling points, and brand references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill to turn product photos and seller-supplied facts into a concise Taobao or Tmall listing video. It helps plan a product-led opening, detail or use moment, clean ending, paid Beatra generation route, delivery, and recovery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a broad Beatra Device Token under ~/.beatra for MCP access.

Mitigation: Install only if Beatra authorization on this device is acceptable, keep the credential private, use the bundled authorization flow, and revoke access from the Beatra Console or bundled uninstall workflow when access is no longer needed.

Risk: The skill uploads product media to Beatra for generation.

Mitigation: Use only product media the user is entitled to upload, inspect local media before upload, and avoid exposing private prompts, credentials, or sensitive input content in chat, logs, command arguments, or environment variables.

Risk: The bundled client silently checks for and may install package updates by default.

Mitigation: Review the update behavior before installation and run `python3 scripts/mcp_client.py update --auto off` if automatic local file replacement is not acceptable.

Risk: Billable Beatra generation requests can create charges or duplicate work if retried incorrectly.

Mitigation: Show a paid admission card before each paid stage, create one stable client_request_id per approved paid request, poll the original task, and retry only the identical frozen request when the original creation outcome is genuinely uncertain.

## Reference(s):

- [Taobao main product video workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/taobao-main-video-maker)
- [Beatra skill homepage](https://beatra.ai/skills/taobao-main-video-maker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes product video plans, paid admission cards, MCP command payloads, polling and recovery steps, and returned artifact details.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
