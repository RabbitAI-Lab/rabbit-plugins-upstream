## Description:

Zoho Recruit API integration with managed OAuth for reading, creating, updating, and searching recruitment records through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and operations users use this skill to let an agent work with Zoho Recruit modules such as candidates, job openings, applications, interviews, and related records. It is intended for account-scoped API work where reads are preferred first and changes require user review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Recruit records can contain sensitive candidate and recruitment data.

Mitigation: Limit retrieval to records needed for the task, summarize rather than exposing full records when possible, and require explicit approval before transferring records to another app or destination.

Risk: Writes, deletions, bulk operations, and new account connections can change or remove recruitment data.

Mitigation: Review the target records, payload, and intended effect before approval; confirm destructive or bulk operations with record-level specificity.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or copied output when raw HTTP access is used.

Mitigation: Prefer managed OAuth through the Maton CLI and avoid printing, persisting, or passing API keys on command lines.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-recruit)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Recruit API v2 Overview](https://www.zoho.com/recruit/developer-guide/apiv2/)
- [Zoho Recruit Get Records API](https://www.zoho.com/recruit/developer-guide/apiv2/get-records.html)
- [Zoho Recruit Insert Records API](https://www.zoho.com/recruit/developer-guide/apiv2/insert-records.html)
- [Zoho Recruit Update Records API](https://www.zoho.com/recruit/developer-guide/apiv2/update-records.html)
- [Zoho Recruit Delete Records API](https://www.zoho.com/recruit/developer-guide/apiv2/delete-records.html)
- [Zoho Recruit Search Records API](https://www.zoho.com/recruit/developer-guide/apiv2/search-records.html)
- [Zoho Recruit Modules API](https://www.zoho.com/recruit/developer-guide/apiv2/modules-api.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed Zoho Recruit API calls, request payloads, result summaries, and user-confirmation prompts.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
