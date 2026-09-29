## Description:

Guides agents in reading and managing Coda docs, pages, tables, rows, and formulas through a user-authorized Maton connection, with optional hosted automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to inspect and, with approval, change Coda content and sharing settings. They can also request scheduled or event-driven Coda actions through Maton functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Coda writes and sharing changes can alter or expose user data.

Mitigation: Confirm the account, target resource, payload, and intended effect before each write or permissions change.

Risk: Hosted functions, triggers, and destinations can run persistently or forward event data.

Mitigation: Approve each automation separately after reviewing its code, schedule or event scope, destination host, data fields, and cleanup plan.

Risk: Broad connections or event scopes can expose more data than the task needs.

Mitigation: Use least-privilege access and narrowly scoped triggers, and remove unused connections and automation.

## Reference(s):

- [Coda API documentation](https://coda.io/developers/apis/v1)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Coda skill listing](https://clawhub.ai/byungkyu/skills/coda-api)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account and network access; modifying resources or enabling automation requires user approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
