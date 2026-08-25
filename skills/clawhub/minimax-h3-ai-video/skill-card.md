## Description:

Create polished 720p or 2K MiniMax H3 videos from written briefs, images, first and last frames, or ordered image, video, and audio references through Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, ecommerce teams, brand teams, game UI designers, and social content producers use this skill to plan, price, submit, track, and review MiniMax H3 video generation work from text or media-based creative inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device token stored under the user's home directory.

Mitigation: Install only when the user accepts that access, keep the token out of chat, logs, command arguments, and environment variables, and use the bundled authorization and disconnect flows for recovery or removal.

Risk: The skill can upload selected local media to Beatra for video generation.

Mitigation: Upload only user-approved image, video, or audio files, preserve returned artifact references, and avoid describing private media facts the host cannot actually perceive.

Risk: The installed package silently checks for and applies verified updates by default.

Mitigation: Disable automatic checks with `python3 scripts/mcp_client.py update --auto off` when silent package replacement is not acceptable, and rely on documented integrity checks for enabled updates.

Risk: Paid video generation can create charges or duplicate work if a request is replayed incorrectly.

Mitigation: Show the live price estimate before billable submission, wait for explicit balance or top-up confirmation, use one stable client request ID per logical request, and retry uncertain submissions only with unchanged arguments.

## Reference(s):

- [MiniMax H3 AI Video Creator on ClawHub](https://clawhub.ai/beatra-ai/skills/minimax-h3-ai-video)
- [MiniMax H3 AI Video homepage](https://beatra.ai/skills/minimax-h3-ai-video)
- [Video routing and H3 controls](references/video-routing.md)
- [MiniMax H3 workflow](references/workflow.md)
- [MiniMax H3 media requirements](references/media-requirements.md)
- [Scene craft for MiniMax H3](references/scene-craft.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Installation registration](references/installation-registration.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)
- [Beatra asset and task management](https://beatra.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit Beatra MCP calls that create, poll, cancel, or recover video generation tasks after user confirmation.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
