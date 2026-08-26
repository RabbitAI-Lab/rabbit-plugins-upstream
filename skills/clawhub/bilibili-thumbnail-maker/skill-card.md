## Description:

Create a Bilibili video cover or Bilibili thumbnail from a topic, title, script, key frame, portrait, product photo, or reference image. This AI thumbnail maker builds a strong focal visual, readable hierarchy, and headline-safe space for Bilibili creators, explainers, tech reviews, lifestyle vlogs, games, food, and entertainment videos, then refines an accepted draft into a repeatable channel look.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Bilibili creators, channel teams, and agents use this skill to plan, generate, compose, or refine one video thumbnail or cover image from a topic, title, script, key frame, portrait, product photo, reference image, or accepted draft. The workflow confirms the prompt, canvas, model, image order, controls, and count before a paid Beatra generation call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra Device Token with broad media, task, artifact, and wallet-spend scopes.

Mitigation: Install only when that shared authorization is acceptable, keep the token private under ~/.beatra, and use the bundled authorization or uninstall scripts rather than copying or deleting credential files manually.

Risk: Default-on silent package updates can replace package-owned files after installation.

Mitigation: Disable automatic updates with python3 scripts/mcp_client.py update --auto off, or use the bundled update check before allowing a replacement.

Risk: Paid image requests can spend Beatra credits, and changed retries can create new paid work.

Mitigation: Freeze the prompt, canvas, image order, model, controls, and count before submission, and reuse a client_request_id only for an identical recovery retry.

Risk: Selected images and limited installation or platform metadata are sent to Beatra during use.

Mitigation: Use only images the user is comfortable uploading and avoid including sensitive content in prompts or source images.

## Reference(s):

- [Workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/bilibili-thumbnail-maker)
- [Beatra skill homepage](https://beatra.ai/skills/bilibili-thumbnail-maker)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON request bodies; successful runs return Beatra task and artifact details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create paid Beatra image generation, transform, or edit tasks and return artifact links, dimensions, task ID, resolved model, and billing.net_charged_credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
