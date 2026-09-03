## Description:

Create a WeChat Channels video cover, WeChat Video Account cover, or WeChat Channels thumbnail from a video topic, title, script, key frame, portrait, product photo, or reference image, with a clear focal visual, a text-safe area, and a channel-consistent cover direction for WeChat Channels videos, creator updates, product explainers, local-business posts, and knowledge content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan, generate, transform, or refine one WeChat Channels video cover with a clear focal visual and title-safe area before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broad shared device authorization for Beatra tools.

Mitigation: Install only when that shared authorization is acceptable, keep the token in the private credential file, and revoke the Beatra device connection when it is no longer needed.

Risk: The security evidence flags registration telemetry and default silent self-updates.

Mitigation: Review the update behavior before installing and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when silent package replacement is not acceptable.

Risk: Uploaded portraits, product photos, key frames, and prompts may contain sensitive or confidential content.

Mitigation: Avoid uploading sensitive media unless Beatra handling is acceptable for the intended use.

Risk: Paid image generation, transform, and edit calls can create duplicate charges if a request is repeated incorrectly.

Mitigation: Require explicit approval of the frozen request, use one opaque `client_request_id`, poll the saved task, and retry only byte-identical uncertain submissions with the same request identity.

Risk: Generated covers can have poor crop safety, low safe-area contrast, or incorrect visible text.

Mitigation: Review the returned image for focal recognition, safe-area contrast, crop risk, must-keep details, and any requested visible text before delivery.

## Reference(s):

- [WeChat Channels cover workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wechat-channels-cover-maker)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/wechat-channels-cover-maker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one-image generation, transform, or edit guidance and returns task, artifact, model, dimension, and billing details when a Beatra task completes.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
