## Description:

Turn seller-supplied SKU specs into one SKU comparison chart set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, commerce teams, and their agents use this skill to plan and produce 4 to 8 SKU comparison stills from confirmed seller-supplied spec rows, keeping one output image per comparison axis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent shared Beatra device credential with broad account capabilities.

Mitigation: Install and run it only when the publisher is trusted, keep credentials out of prompts and logs, and revoke the device authorization from the Beatra Console when no longer needed.

Risk: Silent automatic updates can change package behavior after installation.

Mitigation: Use the documented update controls to disable automatic updates with scripts/mcp_client.py update --auto off when a fixed reviewed version is required.

Risk: Local file uploads may expose sensitive product or reference material.

Mitigation: Inspect files before upload, avoid sensitive local files, and upload only the references needed for the approved SKU chart work.

Risk: Paid image generation and recovery flows can create unwanted charges if requests are replayed incorrectly.

Mitigation: Use one opaque client_request_id per unchanged request, recover uncertain responses with the same arguments, and start changed work only after fresh user approval.

## Reference(s):

- [SKU comparison workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON and shell command examples; generated comparison stills are delivered as image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires confirmed SKU names, seller-supplied spec rows, and an approved chart count before paid image generation.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
