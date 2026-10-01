## Description:

Guides administrators through reading and managing Google Workspace users, groups, organizational units, roles, and domains through a managed connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Google Workspace administrators use this skill to inspect and manage directory resources through Maton, with explicit confirmation before administrative changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative changes to users, groups, policies, or domains can have widespread or irreversible effects.

Mitigation: Use a least-privileged admin connection and require explicit confirmation of the exact method, endpoint, target, and consequences before every write.

Risk: Hosted functions, triggers, or destinations can continue acting or forwarding data after a task ends.

Mitigation: Avoid broad automation and review or delete functions, triggers, and destinations when they are no longer needed.

Risk: An unused OAuth connection can retain administrative access.

Mitigation: Restrict OAuth scopes to the task and revoke the connection when administrative work is complete.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/google-workspace-admin)
- [Google Admin SDK overview](https://developers.google.com/admin-sdk)
- [Google Directory API reference](https://developers.google.com/admin-sdk/directory/v1/guides)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include administrative request details and resource identifiers for user review before execution.]

## Skill Version(s):

1.2.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
