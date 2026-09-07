## Description:

Turns authorized community event site photos and office-supplied facts into one silent 2-15 second community site clip per photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and community offices use this skill to plan and generate one short, silent motion clip for each authorized event-site photo, using only office-supplied facts and preserving photo order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a broad shared Beatra Device Token for authenticated tool access, including wallet spend and task operations.

Mitigation: Install only in an environment where shared Beatra access and wallet use are acceptable; keep the token in the documented private credential file and revoke or reconnect through the documented Beatra flow when needed.

Risk: Silent package self-updates are enabled by default.

Mitigation: Review the automatic update behavior before installation and disable it with the documented update command when silent updates are not acceptable.

Risk: Billable video generation can duplicate cost if transport recovery is handled incorrectly.

Mitigation: Use one frozen client request identity per paid photo, avoid replacement submissions while a task is queued or running, and report only returned usage and net charged credits.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/community-site-clip)
- [Beatra skill homepage](https://beatra.ai/skills/community-site-clip)
- [Community site one-shot workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one silent 2-15 second clip per input photo; generated video task results are reported in photo order with usage and net charged credits when returned.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
