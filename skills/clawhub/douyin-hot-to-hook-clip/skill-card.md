## Description:

Turn a Douyin hot search topic into one talking hook clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and their agents use this skill to turn seller-approved Douyin hot-search topics, brand facts, and still images into short talking hook clips. It supports planning, optional hot-search lookup, voice or speech generation, image-to-video animation, task polling, and billing-aware recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared local Beatra bearer token with broad access across Beatra skills on the device.

Mitigation: Install only when that shared credential model is acceptable, keep the credential private, and avoid exposing it in chat, command arguments, logs, environment variables, or copied files.

Risk: The skill can spend Beatra credits for lookup, voice, speech, and video stages after user confirmations.

Mitigation: Require a separate approval card for each paid stage, quote live prices, use one opaque request ID per approved call, and report actual net charged credits from terminal task results.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates when deterministic local behavior is required, and rely on the bundled verification and rollback controls for update safety.

Risk: The workflow uploads selected media and may use likeness or voice material.

Mitigation: Use only inspected, authorized media; confirm likeness and voice rights before clone or animation stages; and upload local files only through the bundled client.

## Reference(s):

- [Douyin Hot Search Hook Clips](SKILL.md)
- [Douyin hot-search hook workflow](references/workflow.md)
- [Douyin hot-search lookup](references/trend-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/douyin-hot-to-hook-clip)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-hot-to-hook-clip)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent through staged approvals, Beatra MCP calls, asynchronous task polling, returned media artifacts, and billing status reporting.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
