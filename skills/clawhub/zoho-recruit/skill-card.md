## Description:

Zoho Recruit API integration with managed OAuth for managing candidates, job openings, interviews, applications, and recruitment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and their agents use this skill to read, create, update, search, and delete Zoho Recruit records through Maton-managed OAuth. It is suited for scoped recruiting workflows involving candidates, job openings, interviews, applications, and approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Recruit records may include applicant PII and other sensitive recruiting data.

Mitigation: Use read/list calls first, limit returned fields to the task, avoid logging raw responses, and only authorize the Zoho account and scopes needed.

Risk: Writes, deletions, new connections, functions, triggers, and destinations can change data or continue operating after setup.

Mitigation: Confirm the exact account, connection, endpoint, payload, handler, trigger, and destination before execution; approve deletions record by record.

Risk: The generic Maton API path can reach Zoho Recruit endpoints beyond the reviewed examples.

Mitigation: Use documented paths as written and require an explicit user request and approval before any undocumented endpoint or high-impact operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-recruit)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
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
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Gmail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, Zoho Recruit API paths, function examples, trigger setup guidance, and approval checklists.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
