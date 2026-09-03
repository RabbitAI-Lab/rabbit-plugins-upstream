## Description:

Turn authorized blackboard photos and teacher-supplied facts into one blackboard one-shot clip per photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and agents use this skill to turn authorized classroom blackboard photos plus teacher-supplied facts into one short silent blackboard clip per photo, delivered in capture order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authorizes broad Beatra account capabilities that can spend credits and access multiple generation and task tools.

Mitigation: Install and authorize it only when that shared Beatra device authorization is acceptable; require explicit user confirmation before each paid video generation.

Risk: Authorized photos are uploaded to Beatra for generation.

Mitigation: Use only photos the user has authorized for this board set and do not reuse file access as consent for unrelated work.

Risk: The bundled client can silently replace package-owned files through automatic updates.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when silent package replacement is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/blackboard-one-shot)
- [Beatra skill homepage](https://beatra.ai/skills/blackboard-one-shot)
- [Blackboard one-shot workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces clip plans, confirmation text, Beatra MCP client commands, task polling guidance, and final clip delivery summaries.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
