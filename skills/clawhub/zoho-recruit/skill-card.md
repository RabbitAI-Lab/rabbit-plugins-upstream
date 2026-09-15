## Description:

Zoho Recruit API integration with managed OAuth for reading, creating, updating, and searching recruitment data through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting operators, developers, and agents use this skill to query and manage Zoho Recruit candidates, job openings, interviews, applications, and approved recruitment workflows through Maton with managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting broader Zoho Recruit scopes or accounts than needed can expose unnecessary recruitment data.

Mitigation: Use only the Zoho Recruit account and scopes needed for the task and confirm any new connection with the user.

Risk: Write and delete operations can modify or irreversibly remove recruiting records.

Mitigation: Default to read-only calls and require explicit confirmation for every write or deletion, reviewing deletions record by record.

Risk: Hosted functions, triggers, and destinations can create persistent automation beyond a single agent turn.

Mitigation: Review and approve each automation before deployment, prefer pinned installs, and remove persistent functions, triggers, or destinations when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-recruit)
- [Maton Homepage](https://maton.ai)
- [Zoho Recruit API v2 Overview](https://www.zoho.com/recruit/developer-guide/apiv2/)
- [Zoho Recruit Get Records API](https://www.zoho.com/recruit/developer-guide/apiv2/get-records.html)
- [Zoho Recruit Insert Records API](https://www.zoho.com/recruit/developer-guide/apiv2/insert-records.html)
- [Zoho Recruit Update Records API](https://www.zoho.com/recruit/developer-guide/apiv2/update-records.html)
- [Zoho Recruit Delete Records API](https://www.zoho.com/recruit/developer-guide/apiv2/delete-records.html)
- [Zoho Recruit Search Records API](https://www.zoho.com/recruit/developer-guide/apiv2/search-records.html)
- [Zoho Recruit Modules API](https://www.zoho.com/recruit/developer-guide/apiv2/modules-api.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with inline shell, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should favor read-only Zoho Recruit calls first and require explicit user confirmation before writes, deletions, new connections, hosted functions, triggers, or destinations.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
