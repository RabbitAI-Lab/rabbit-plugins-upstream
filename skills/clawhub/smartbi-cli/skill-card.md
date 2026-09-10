## Description:

smartbi-cli helps agents discover, inspect, and call Smartbi OpenAPI operations for BI analysis, data queries, modeling, scheduling, messaging, and permission workflows through the @smartbi/cli tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wahsonleung](https://clawhub.ai/user/wahsonleung)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and BI operators use this skill to let an agent translate Smartbi business requests into CLI discovery, contract inspection, API calls, scheduled tasks, and outbound message workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad Smartbi authority across BI data, modeling, scheduling, resource management, permissions, and messaging workflows.

Mitigation: Review requested operations and require explicit confirmation before write, schedule, permission, or outbound messaging actions.

Risk: Smartbi tokens may be stored in local configuration or passed during setup.

Mitigation: Review token scope before installation and prefer environment-variable or keyring-based credentials where possible.

Risk: Scheduled jobs and outbound messages can send BI data outside Smartbi through email or webhook recipients.

Mitigation: Confirm recipients, webhook URLs, schedules, and data payloads before execution.

Risk: The skill depends on installing and running the external @smartbi/cli npm package.

Mitigation: Review the npm CLI source and use a pinned, reviewed CLI version from a trusted installation path.

Risk: Connecting to untrusted or non-HTTPS Smartbi endpoints may expose credentials or BI data.

Mitigation: Use HTTPS-only trusted Smartbi or SDK Server endpoints unless a reviewer approves a controlled exception.

## Reference(s):

- [Smartbi CLI Skill](README.md)
- [init / installation and configuration reference](references/init.md)
- [profile environment reference](references/profiles.md)
- [list / search discovery reference](references/discovery.md)
- [describe contract reference](references/describe.md)
- [call execution reference](references/call.md)
- [strategy reference](references/strategy.md)
- [domain documentation index](references/doc-index.md)
- [Rhino MQL script template](references/rhino-template.md)
- [scheduled task scenario](scenarios/schedule-task.md)
- [message push scenario](scenarios/push-message.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Smartbi CLI commands, JSON request body files, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create temporary JSON request body files and Smartbi configuration profiles when needed.]

## Skill Version(s):

2.0.0 (source: release evidence and user changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
