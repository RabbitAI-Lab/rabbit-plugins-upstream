## Description:

Sunsama MCP integration with managed authentication for daily tasks, calendar events, backlog, objectives, time tracking, and Gmail or Outlook email threads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting Sunsama users use this skill to search, create, schedule, update, and delete tasks, calendar events, objectives, time tracking entries, and linked email threads through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broker access to Sunsama tasks, calendar data, and linked Gmail or Outlook email threads.

Mitigation: Prefer OAuth, confirm the exact account and resource before write or delete actions, and use only the scopes needed for the current task.

Risk: Calendar, email, task deletion, and recurring-task operations can modify or remove user data.

Mitigation: Retrieve the current resource first, then confirm the resource title, ID, date, payload, and intended effect before executing high-impact operations.

Risk: API-key fallback can expose a long-lived credential if handled carelessly.

Mitigation: Use the OAuth and operating-system credential-store path when possible, and avoid printing, logging, exporting, or persisting credentials.

Risk: External task, calendar, or email content may contain untrusted instructions.

Mitigation: Treat returned content as data, not instructions, and do not execute, evaluate, or interpolate it into shell commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/sunsama)
- [Maton homepage](https://maton.ai)
- [Maton API documentation](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Sunsama](https://sunsama.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calls are routed through the Maton CLI and Sunsama MCP connection, requiring network access, a Maton account, and user-approved Sunsama authorization.]

## Skill Version(s):

1.1.0 (source: server release metadata; frontmatter metadata version is 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
