## Description:

Turn a user-supplied public trading calendar and authorized stills into one trading calendar talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Wealth advisors and educators use this skill to turn public trading calendar entries and authorized still images into short talking calendar clips. It helps plan calendar-read slots, confirm paid voice or video stages, and deliver one clip per still without inventing market dates or trading guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a reusable Beatra Device Token for broad account access.

Mitigation: Install only after review, keep the credential in the private Beatra credential file, do not expose tokens in chat or command arguments, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The skill can upload local media files and spend Beatra credits through remote generation tools.

Mitigation: Use only authorized stills, voice samples, and public calendar facts; show separate confirmation cards before clone, speech, and video calls; use one opaque client_request_id per paid request.

Risk: Silent package self-updates are enabled by default.

Mitigation: Review the update behavior before installing and run `python3 scripts/mcp_client.py update --auto off` when automatic package replacement is not acceptable.

Risk: Calendar clips could misstate dates, holidays, settlement timing, or trading facts if unsupported details are added.

Mitigation: Speak only dates and session facts already printed on the supplied public calendar and review each final clip for identity, speech clarity, mouth timing, and calendar accuracy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/market-calendar-talking)
- [Beatra skill homepage](https://beatra.ai/skills/market-calendar-talking)
- [Calendar talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces labeled clip plans, approval cards, Beatra MCP call payloads, task recovery guidance, and delivery notes for generated audio or video artifacts.]

## Skill Version(s):

0.1.3 (source: server evidence release.version and artifact manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
