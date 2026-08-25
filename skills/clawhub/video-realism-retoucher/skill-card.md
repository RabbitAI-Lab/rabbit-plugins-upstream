## Description:

Polish an existing AI-generated short video with a focused realism retouch for lighting, material texture, color saturation, or repeated-detail issues while preserving the source clip's subject, framing, timing, and mood.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to prepare one source-led Beatra video edit that makes an existing AI-generated short video look more natural. It guides source inspection, live model admission, prepaid confirmation, submission, polling, and delivery while limiting the work to one focused retouch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra Device Token with broad media-generation authority.

Mitigation: Review the requested authority before installing, keep the token out of chat and logs, and revoke the Beatra device authorization from the Beatra Console when the skill is no longer needed.

Risk: The bundled client can check for and install package updates silently before ordinary Beatra commands.

Mitigation: Disable silent update checks with `python3 scripts/mcp_client.py update --auto off`, or inspect the official available version with `python3 scripts/mcp_client.py update --check` before use.

Risk: A video retouch is billable and transport uncertainty can otherwise lead to duplicate paid work.

Mitigation: Show the prepaid admission card before submission, submit once with one `client_request_id`, poll the original task, and retry only the identical request with the same ID when delivery is uncertain.

Risk: The agent may not be able to visually verify the source or returned video in every host environment.

Mitigation: When the source or result is not viewable, report task and artifact facts only and mark visual review incomplete rather than claiming the retouch quality was inspected.

## Reference(s):

- [Focused video realism retouch workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/video-realism-retoucher)
- [Beatra skill homepage](https://beatra.ai/skills/video-realism-retoucher)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one focused Beatra video-edit workflow with task, artifact, usage, and billing facts; it does not directly render video in chat.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
