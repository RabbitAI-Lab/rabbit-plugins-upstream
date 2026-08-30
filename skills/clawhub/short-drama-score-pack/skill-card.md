## Description:

Build an original short-drama score pack of 8 to 15 instrumental beds for tension, romance, comedy, and tearjerker scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and agent operators use this skill to plan, price, generate, poll, and review a labeled pack of instrumental background music beds for vertical short-drama episodes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account permissions beyond music generation.

Mitigation: Review the requested OAuth scopes before authorizing and install only when the account-level access is acceptable.

Risk: The skill stores a shared local Beatra device token.

Mitigation: Keep the credential file private, avoid copying tokens into chat or logs, and use the documented uninstall flow when disconnecting the device.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Use the documented update command to disable automatic updates when change control or manual review is required.

Risk: Music generation consumes Beatra credits and transport uncertainty can otherwise cause duplicate paid work.

Mitigation: Confirm the live pack estimate before generation and preserve the same client_request_id when recovering an uncertain paid request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/short-drama-score-pack)
- [Beatra package page](https://beatra.ai/skills/short-drama-score-pack)
- [Short-drama score workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation registration](references/installation-registration.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra task IDs, billing fields, resolved model details, media metadata, and artifact URLs or IDs when generation succeeds.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
