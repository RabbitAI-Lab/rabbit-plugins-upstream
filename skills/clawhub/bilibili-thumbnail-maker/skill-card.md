## Description:

Create a Bilibili video cover or Bilibili thumbnail from a topic, title, script, key frame, portrait, product photo, or reference image. This AI thumbnail maker builds a strong focal visual, readable hierarchy, and headline-safe space for Bilibili creators, explainers, tech reviews, lifestyle vlogs, games, food, and entertainment videos, then refines an accepted draft into a repeatable channel look.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Bilibili creators and channel teams use this skill to create or refine one video thumbnail from a topic, title, script, key frame, portrait, product photo, reference image, or accepted draft. It guides prompt preparation, paid Beatra image generation, result review, and delivery of artifact links with billing and task details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with broad media, task, artifact, and spending-related authority.

Mitigation: Install only after reviewing that authority, keep credentials under ~/.beatra, and reconnect with scripts/authorize.py --force only after an explicit user decision.

Risk: Silent self-updates are enabled by default for the bundled Beatra client.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` before use to disable silent update checks, or use `python3 scripts/mcp_client.py update --check` for a manual version check.

Risk: First use registers package, version, platform, and installation data with Beatra.

Mitigation: Review the registration behavior before installation; registration failures should not block the requested creative task.

Risk: Generation requests consume Beatra credits and duplicate submissions can create additional paid work.

Mitigation: Freeze the prompt, canvas, image order, model, controls, and count before approval; submit once with a stable client_request_id and retry only an identical payload with the same request identity after transport uncertainty.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/bilibili-thumbnail-maker)
- [Beatra package homepage](https://beatra.ai/skills/bilibili-thumbnail-maker)
- [Workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated image artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, observed dimensions, resolved model, billing.net_charged_credits, and one focused unexecuted refinement suggestion.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
