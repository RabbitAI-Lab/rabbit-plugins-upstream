## Description:

Helps agents manage Firebase projects and web, Android, and iOS apps through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to list Firebase projects, manage app registrations and configurations, and link Google Analytics with their authorized accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a connection may grant Maton access to a Firebase account.

Mitigation: Confirm the intended account and required access before connecting; review how to revoke authorization.

Risk: Writes, hosted functions, and persistent triggers can change projects or run actions later.

Mitigation: Get explicit approval after checking the exact project, operation, and trigger behavior.

Risk: Sending data to a third-party destination may expose project information.

Mitigation: Review the destination and the data that will flow there before approval.

## Reference(s):

- [ClawHub firebase skill](https://clawhub.ai/byungkyu/skills/firebase)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Firebase Management API overview](https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project)
- [Firebase Management REST API reference](https://firebase.google.com/docs/reference/firebase-management/rest)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Firebase operations require an authorized Maton connection; writes require user confirmation.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
