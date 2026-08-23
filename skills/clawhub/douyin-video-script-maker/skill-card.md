## Description:

Create a Douyin short-video script, Douyin spoken script, or Douyin product-video script from a topic, product or service facts, audience, and creator voice. This AI Douyin script writer produces three hook options, a ready-to-film short-video script, shot-by-shot beats, natural spoken lines, subtitle cues, title ideas, hashtags, and a comment prompt for knowledge sharing, local business, product demos, reviews, unboxings, shop content, and creator series. The chosen title then becomes a matching vertical 9:16 Douyin cover with a headline-safe composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, social media marketers, local businesses, and product teams use this skill to turn a Douyin topic or product brief into a filming-ready short-video script with hooks, spoken lines, shot beats, subtitle cues, titles, hashtags, and a comment prompt. After the written script is approved, the skill can offer one paid 9:16 cover image derived from the chosen title and script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device connection with broad media and wallet authority.

Mitigation: Install only if that authority is acceptable, review Beatra device revocation behavior, and uninstall through the bundled workflow so shared credentials are not removed while other Beatra skills still use them.

Risk: The bundled client checks for silent package updates by default.

Mitigation: Disable automatic update checks for the installation with `python3 scripts/mcp_client.py update --auto off` when silent updates are not acceptable.

Risk: Paid image generation can create duplicate charges if uncertainty is handled as a new request.

Mitigation: Use one stable client_request_id for each approved cover request, retry only the identical frozen payload under that ID, and poll existing task IDs before considering any replacement work.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/douyin-video-script-maker)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-video-script-maker)
- [Douyin short-video script workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured script sections and inline shell commands for optional Beatra tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, artifact links, returned dimensions, resolved model, and billing.net_charged_credits when a paid cover generation is approved and completed.]

## Skill Version(s):

0.1.5 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
