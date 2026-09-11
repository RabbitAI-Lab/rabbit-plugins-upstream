## Description:

Creates MiniMax H3 videos from text prompts, images, first and last frames, or multimodal references, with guidance for routing, cost confirmation, submission, tracking, and delivery through a Beatra account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, ecommerce teams, brand teams, and agent users use this skill to turn prompts or supplied media into short MiniMax H3 videos. It helps the agent choose the right generation route, prepare media, confirm live cost facts, submit one paid request, recover safely, and report finished artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad Beatra account authority through a shared local device token.

Mitigation: Install only if the publisher is trusted, keep the credential file private to the current user, and reconnect authorization only when the user explicitly approves it.

Risk: The packaged client can silently check for and install verified updates before ordinary Beatra commands.

Mitigation: Review this update behavior before installation and disable automatic checks with `python3 scripts/mcp_client.py update --auto off` when silent updates are not acceptable.

Risk: Video generation is paid work and duplicate submissions can create unintended charges.

Mitigation: Require a live model-card estimate, explicit top-up or balance confirmation, and one stable `client_request_id`; recover uncertain submissions only with byte-equivalent arguments.

Risk: Local media uploaded for generation becomes available to Beatra's remote tools.

Mitigation: Upload only user-approved media, preserve returned artifact references, and avoid exposing tokens, full private prompts, or sensitive input content in logs or chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/minimax-h3-ai-video)
- [Beatra skill homepage](https://beatra.ai/skills/minimax-h3-ai-video)
- [MiniMax H3 workflow](references/workflow.md)
- [Video routing and H3 controls](references/video-routing.md)
- [MiniMax H3 media requirements](references/media-requirements.md)
- [Scene craft for MiniMax H3](references/scene-craft.md)
- [Review and recovery](references/review-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Installation registration](references/installation-registration.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans and executes one logical video request at a time, then reports task IDs, artifact links, observed media facts, and billing fields when available.]

## Skill Version(s):

0.1.5 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
