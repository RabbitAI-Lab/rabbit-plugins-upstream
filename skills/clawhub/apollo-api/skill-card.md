## Description:

Helps agents search and enrich Apollo people and organizations and manage sales records through an authorized account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and operations teams use this skill to prospect, enrich leads, and manage contacts and accounts in their connected Apollo account. With separate approval, they can configure functions and triggers for ongoing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected-account requests can access or change Apollo sales and personal data.

Mitigation: Use the intended account and minimum necessary data; confirm the records and effect before each write.

Risk: Hosted functions and triggers can keep running and forward data after setup.

Mitigation: Approve the function, trigger, destination and data flow explicitly; review how to disable or remove them.

Risk: Fallback HTTP access uses a long-lived API key that could be exposed.

Mitigation: Prefer managed login; when fallback access is necessary, keep the key out of logs, files and command lines.

## Reference(s):

- [Apollo skill release](https://clawhub.ai/byungkyu/skills/apollo-api)
- [Maton homepage](https://maton.ai)
- [Apollo API reference](https://docs.apollo.io/reference)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with shell and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include contact or account data; writes and automation require user approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
