## Description:

Helps administrators manage Dropbox Business teams, files, and audit activity through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Dropbox Business administrators use this skill to inspect and manage team members, groups, folders, devices, sharing, audit logs, and member files, with approval before changes or sensitive access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Admin access can alter or permanently delete team resources.

Mitigation: Use the least-privileged admin account, review OAuth scopes, and confirm exact resource identifiers and consequences before writes or deletes.

Risk: Access to individual members' files and audit data can expose sensitive information.

Mitigation: Access member files only on explicit request with a stated business justification; limit retrieved data to what the task needs.

Risk: Unused connections and automations may retain access or continue acting on events.

Mitigation: Remove unused connections, functions, triggers, and destinations when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/dropbox-business)
- [Maton homepage](https://maton.ai)
- [Dropbox Business API documentation](https://www.dropbox.com/developers/documentation/http/teams)
- [Dropbox team administration guide](https://developers.dropbox.com/dbx-team-administration-guide)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with shell examples and optional JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized Dropbox Business connection and network access.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
