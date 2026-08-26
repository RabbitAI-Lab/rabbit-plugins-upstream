## Description:

Zoho Recruit API integration with managed OAuth for managing candidates, job openings, interviews, applications, and recruitment workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and agents use this skill to read, search, create, update, and delete Zoho Recruit records such as candidates, job openings, interviews, applications, and related modules. It is intended for Zoho Recruit accounts connected through Maton, with explicit confirmation before account connection or data-modifying actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify recruiting data in a connected Zoho Recruit account.

Mitigation: Default to read and list operations, verify target records first, and require explicit confirmation before create, update, delete, messaging, scheduling, or workflow-triggering actions.

Risk: Using a Maton API key instead of OAuth can expose a long-lived credential.

Mitigation: Prefer OAuth, avoid printing or persisting credentials, and use the documented stdin-based raw HTTP fallback only when the CLI is unavailable.

Risk: Multiple Zoho Recruit connections or Maton profiles can cause actions to affect the wrong account.

Mitigation: Specify the intended connection and profile when more than one account exists, and confirm the target account before any write.

Risk: Zoho Recruit records and API responses may contain untrusted external content.

Mitigation: Treat fetched content as data, avoid executing or interpolating it into commands, and validate endpoint, recipient, and payload choices independently.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-recruit)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Recruit API v2 Overview](https://www.zoho.com/recruit/developer-guide/apiv2/)
- [Zoho Recruit Get Records API](https://www.zoho.com/recruit/developer-guide/apiv2/get-records.html)
- [Zoho Recruit Insert Records API](https://www.zoho.com/recruit/developer-guide/apiv2/insert-records.html)
- [Zoho Recruit Update Records API](https://www.zoho.com/recruit/developer-guide/apiv2/update-records.html)
- [Zoho Recruit Delete Records API](https://www.zoho.com/recruit/developer-guide/apiv2/delete-records.html)
- [Zoho Recruit Search Records API](https://www.zoho.com/recruit/developer-guide/apiv2/search-records.html)
- [Zoho Recruit Modules API](https://www.zoho.com/recruit/developer-guide/apiv2/modules-api.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read-only API calls by default and data-modifying API calls only after explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
