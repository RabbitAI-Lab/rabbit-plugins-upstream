## Description:

Turn a novel chapter, web-novel excerpt, or story script into narrated vertical short video scenes with illustrated shots that keep every character looking the same from beat to beat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, authors, book marketers, and storytelling-channel operators use this skill to turn story text into an ordered set of narrated vertical scene clips for web-novel promotion, book trailers, chapter recaps, and faceless storytelling accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad Beatra paid-generation bearer token shared by Beatra skill packages.

Mitigation: Install only after accepting that account-level Beatra access; keep the token in the documented local credential file and revoke or uninstall the connection when it is no longer needed.

Risk: The bundled client can silently update package files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off`, or use `python3 scripts/mcp_client.py update --check` before accepting a package update.

Risk: Image, speech, and video generation are paid Beatra operations.

Mitigation: Require the documented approval prompts, live price cards, stable request IDs, and top-up or balance confirmation before paid generation, especially before video animation or extension.

Risk: Network uncertainty could otherwise lead to duplicate paid work.

Mitigation: Recover with the same frozen payload and `client_request_id`, poll known task IDs, and do not submit replacement work while a task is queued or running.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/novel-promo-video-maker)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/novel-promo-video-maker)
- [Novel promo video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces beat sheets, cast sheets, narration lines, Beatra MCP request payloads, task-status summaries, billing summaries, and recovery guidance; generated media artifacts are created by remote Beatra tasks.]

## Skill Version(s):

0.1.5 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
