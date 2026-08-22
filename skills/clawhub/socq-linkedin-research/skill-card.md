## Description:

Research public LinkedIn content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and business analysts use this skill to select and run SocQ LinkedIn endpoints for public LinkedIn discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, and exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn research targets, queries, filters, task metadata, and SocQ API-authenticated requests are sent to SocQ.

Mitigation: Use the skill only when this data sharing is acceptable, and avoid submitting confidential case details or secrets as research prompts.

Risk: Large or multi-endpoint runs can consume SocQ credits.

Mitigation: Check expected credit costs and confirm scope before starting paid large-volume or multi-endpoint collection.

Risk: Results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report task status, pages read, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

Risk: A SocQ API key is required for CLI, MCP, and REST requests.

Mitigation: Keep SOCQ_API_KEY in the environment and do not place it in prompts, URLs, committed files, or retained commands.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ LinkedIn API](https://socq.ai/apis/linkedin)
- [SocQ LinkedIn API Documentation](https://docs.socq.ai/api-manual/linkedin)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [LinkedIn Endpoint Registry](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown with endpoint summaries, input and filter details, credit usage, task status, normalized findings, and optional shell commands or API parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination status, collection time, failed requests, unsupported filters, incomplete coverage notes, and raw export locations.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
