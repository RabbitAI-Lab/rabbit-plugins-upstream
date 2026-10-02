## Description:

Helps agents search and manage Google contacts and contact groups through a Maton-managed connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to find, create, update, or delete contacts and organize contact groups in their Google account. The skill also guides user-approved automation through hosted functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A write or delete may change the wrong contact, group, connection, or function.

Mitigation: Confirm the exact account and target with the user before writing or deleting.

Risk: Triggers and destinations may continue to run or forward data after the initial task.

Mitigation: Confirm the trigger schedule and destination before enabling them, and remove them when no longer needed.

## Reference(s):

- [Google People API overview](https://developers.google.com/people/api/rest)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage (skill metadata)](https://maton.ai)
- [Google Contacts skill on ClawHub](https://clawhub.ai/byungkyu/skills/google-contacts)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include contact data returned by authorized requests; limit disclosure to fields needed for the task.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
