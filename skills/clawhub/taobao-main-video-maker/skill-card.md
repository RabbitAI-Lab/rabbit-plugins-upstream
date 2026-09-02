## Description:

Create a Taobao product main-image video or Tmall product main-image video from product photos, selling points, and brand references. This AI product video maker builds a product-led opening, detail or use moment, and clean finish for Taobao product listings, Tmall product pages, ecommerce product listing videos, new-product launches, and seasonal campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and agents use this skill to turn inspectable product photos and seller-provided facts into a short silent Taobao or Tmall product main-image video. It supports planning, paid-stage confirmation, Beatra task submission, polling, delivery, and recovery while keeping product must-keeps central.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a broad reusable local Beatra device token.

Mitigation: Review before installing, keep the credential private, use the bundled uninstall and disconnect flow when access is no longer needed, and do not expose the token in chat, commands, logs, or files outside the private credential store.

Risk: The bundled client silently updates package files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when manual review is required before code changes.

Risk: Selected product media is uploaded to Beatra for remote image or video generation.

Mitigation: Use only product media the user is entitled to provide, inspect local media before upload, and avoid placing credentials or sensitive private prompts in command arguments.

Risk: Paid generation tasks can consume Beatra credits or be duplicated after uncertain transport failures.

Mitigation: Show a paid-stage admission card, wait for explicit user confirmation, use one stable `client_request_id` per frozen request, poll the original task, and retry only byte-identical uncertain submissions with the same request ID.

Risk: Unsupported product, performance, certification, or effect claims could mislead listing viewers.

Mitigation: Use seller-supplied facts for non-visual claims, keep effect claims without evidence at draft, and route live-action editing requests out of this skill.

## Reference(s):

- [Taobao main product video workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/taobao-main-video-maker)
- [Beatra skill page](https://beatra.ai/skills/taobao-main-video-maker)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with inline shell commands and JSON tool payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra artifact IDs or URLs, task IDs, resolved model details, dimensions, duration, usage, and billing fields after confirmed paid remote generation.]

## Skill Version(s):

0.1.4 (source: server release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
