## Description:

Turn a user-supplied fund quarterly report highlight sheet and authorized stills into one fund quarterly report talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisors and fund marketers use this skill to turn supplied quarterly report highlights and authorized stills into 2 to 8 short Beatra talking clips, one clip per still.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization creates a broad shared Beatra device token under ~/.beatra.

Mitigation: Install only when the user trusts Beatra and keep the credential private; revoke the device in the Beatra Console or use the bundled uninstall flow when access is no longer needed.

Risk: Ordinary client commands can silently update local executable skill files by default.

Mitigation: Use python3 scripts/mcp_client.py update --auto off to disable automatic update checks for this installation when a pinned local package is required.

Risk: The workflow can spend Beatra credits for clone, speech, and video generation.

Mitigation: Show the required approval card for each paid stage, use unique client_request_id values, and do not retry uncertain paid requests with changed arguments.

Risk: Fund report clips could imply unsupported financial advice if content is invented beyond the supplied highlights.

Mitigation: Use only facts printed in the user-supplied quarterly highlight sheet and avoid return forecasts, market direction calls, buy or sell recommendations, and unsupported metrics.

## Reference(s):

- [Quarterly report talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans and reports separate talking-clip tasks; paid media generation returns Beatra task and artifact details when available.]

## Skill Version(s):

0.1.2 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
