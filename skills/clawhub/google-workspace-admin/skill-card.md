## Description:

Google Workspace Admin SDK integration with managed OAuth for reading and managing users, groups, organizational units, roles, and domain settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators, IT operators, and developers use this skill to let an agent perform approved Google Workspace administration through Maton, including account, group, organizational unit, role, and domain tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support high-impact Google Workspace administration, including changes to users, groups, roles, organizational units, and domain settings.

Mitigation: Install only for Google Workspace administration, use a least-privileged admin account, confirm every write by exact target and consequence, and avoid broad or bulk changes.

Risk: Long-lived credentials or stale connections can preserve access after the administrative task is complete.

Mitigation: Prefer OAuth over API keys and revoke Maton connections, functions, or triggers when the task is finished.

Risk: Hosted functions or triggers can turn approved actions into continuing automation.

Mitigation: Use user-reviewed handlers, restrict network access where supported, keep destinations within the intended platform flow unless explicitly approved, and confirm each deploy, invocation, or persistent trigger separately.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-workspace-admin)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Admin SDK](https://developers.google.com/admin-sdk)
- [Google Admin SDK Directory API Guides](https://developers.google.com/admin-sdk/directory/v1/guides)
- [Directory API Users](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
- [Directory API Groups](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups)
- [Directory API Members](https://developers.google.com/admin-sdk/directory/reference/rest/v1/members)
- [Directory API Org Units](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits)
- [Directory API Domains](https://developers.google.com/admin-sdk/directory/reference/rest/v1/domains)
- [Directory API Roles](https://developers.google.com/admin-sdk/directory/reference/rest/v1/roles)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, HTTP/API call patterns, and Python function snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write-capable administrative actions are framed for explicit user approval and least-privilege operation.]

## Skill Version(s):

1.2.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
