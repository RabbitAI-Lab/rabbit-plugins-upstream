## Description:

Create a filming-ready Douyin short-video script from a topic, product or service facts, audience, and creator voice, with hooks, spoken lines, shot beats, subtitle cues, title ideas, hashtags, a comment prompt, and an optional matching 9:16 cover.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, social commerce teams, and content marketers use this skill to turn a Douyin topic, product or service brief, audience, and creator voice into a filming-ready short-video script. After the script is complete, the skill can prepare and submit one paid 9:16 cover generation only after the user approves the frozen plan and price.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra device token is shared and broad enough to cover capabilities beyond the Douyin script-and-cover workflow, including billable media operations.

Mitigation: Install only when that access is acceptable, review the Beatra authorization page and account activity, and revoke or uninstall the connection when it is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when a pinned package review is required.

Risk: Optional cover generation consumes Beatra credits and can create duplicate charges if retried incorrectly.

Mitigation: Require a frozen plan, current price or ceiling, and explicit approval before generation; preserve the same opaque `client_request_id` for identical recovery retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/douyin-video-script-maker)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-video-script-maker)
- [Douyin short-video script workflow](artifact/references/workflow.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Image artifacts]

**Output Format:** [Markdown with structured script sections, inline shell commands for Beatra MCP calls, and optional image artifact links after paid cover generation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The main deliverable is free text planning; optional cover generation is asynchronous paid work and should report only returned task, model, dimensions, artifact, usage, and billing facts.]

## Skill Version(s):

0.1.8 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
