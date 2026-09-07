## Description:

Turn authorized blackboard photos and teacher-supplied facts into one blackboard one-shot clip per photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education-content creators use this skill to turn authorized blackboard photos and teacher-supplied lesson facts into one short silent video clip per photo while preserving photo order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with broad generation and wallet-related permissions.

Mitigation: Install only in environments where that account access is acceptable, keep the credential file private, and disconnect or uninstall when access is no longer needed.

Risk: The bundled client silently updates package-owned files by default.

Mitigation: Disable automatic update checks with `python3 scripts/mcp_client.py update --auto off` in sensitive environments, and review updates before use.

Risk: Billable video generation can create charges if a request is submitted after user confirmation.

Mitigation: Show the live price and six-field production card before submitting, use one request identity per photo, and avoid retrying paid requests with changed inputs.

## Reference(s):

- [Blackboard One-Shot Clips on ClawHub](https://clawhub.ai/beatra-ai/skills/blackboard-one-shot)
- [Beatra Skill Homepage](https://beatra.ai/skills/blackboard-one-shot)
- [Blackboard one-shot workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one Beatra video generation request plan per source photo and reports terminal task results, dimensions, duration, usage, and net charged credits.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
