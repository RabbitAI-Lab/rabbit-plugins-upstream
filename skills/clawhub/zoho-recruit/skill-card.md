## Description:

Zoho Recruit API integration with managed OAuth for managing candidates, job openings, interviews, applications, and recruitment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and recruiting operations users use this skill to read, create, update, search, and cautiously delete Zoho Recruit records through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Zoho Recruit recruiting records, including sensitive candidate data.

Mitigation: Use OAuth where possible, select least-privilege Zoho scopes, prefer read-only calls first, and confirm the target account and record identifiers before changes.

Risk: Create, update, and delete actions can change or remove recruiting records; deletions can be bulk and irreversible.

Mitigation: Require explicit user confirmation before every write, and review deletions record by record before execution.

Risk: Long-lived credentials or provider-issued tokens may leak if printed, logged, stored, or passed on command lines.

Mitigation: Keep credentials in the Maton or operating-system credential store, avoid printing or persisting token values, and send gateway credentials only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-recruit)
- [Maton](https://maton.ai)
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

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Zoho Recruit connection.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
