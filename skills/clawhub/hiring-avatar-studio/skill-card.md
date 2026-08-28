## Description:

Turn one HR or founder portrait and a job brief into one talking-avatar hiring video per open role.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

HR teams, recruiters, and founders use this skill to create one role-specific talking-avatar hiring video from an authorized portrait plus a job description, script, or approved speech track. The workflow helps an agent verify likeness and voice rights, prepare narration, create or select a voice, submit paid Beatra generation tasks, and report returned clips with usage and billing facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account authority, including paid-generation authority.

Mitigation: Install only when that authority is acceptable, require explicit user confirmation at each paid boundary, and report live estimates plus final billing facts.

Risk: The skill stores a shared device credential and local state under ~/.beatra.

Mitigation: Use the bundled authorization and uninstall helpers, keep credentials out of chat, logs, command arguments, and environment variables, and revoke the device from the Beatra Console when access should end.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic checks with `python3 scripts/mcp_client.py update --auto off` or run `python3 scripts/mcp_client.py update --check` before updating manually.

Risk: Portrait and voice misuse could occur if a user lacks likeness or voice rights.

Mitigation: Stop before generation unless the user confirms rights for the portrait and voice, and treat access to a file as insufficient proof of consent.

Risk: Retrying uncertain paid requests incorrectly can duplicate work or charges.

Mitigation: Reuse the same `client_request_id` only with an identical payload, poll existing tasks before resubmitting, and create a new request ID only for user-approved changed work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/hiring-avatar-studio)
- [Beatra skill homepage](https://beatra.ai/skills/hiring-avatar-studio)
- [Hiring avatar workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When generation is executed, the skill reports returned video clips with actual dimensions, duration, usage, and billing facts.]

## Skill Version(s):

0.1.1 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
