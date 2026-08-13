## Description:

Research public Instagram content, accounts, keywords, and performance data with SocQ. Use when an agent needs Instagram-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to select and run SocQ Instagram endpoints for public content, account, keyword, and performance research. It helps estimate credits, submit asynchronous tasks, follow pagination, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public Instagram targets, query terms, filters, and task data are sent to SocQ under the user's account.

Mitigation: Use the skill only for appropriate public-data research, keep SOCQ_API_KEY out of prompts and committed files, and confirm that sending the requested data to SocQ is acceptable.

Risk: Large-volume or multi-endpoint SocQ runs can consume credits.

Mitigation: Check expected endpoint cost and account limits before execution, reduce scope when needed, and require user confirmation before paid large-volume or multi-endpoint runs.

Risk: Research coverage can be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report result counts, pages read, remaining pagination state, failed requests, unsupported filters, and any incomplete coverage in the final output.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Instagram API](https://docs.socq.ai/api-manual/instagram)
- [SocQ Instagram Platform](https://socq.ai/apis/instagram)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Instagram Endpoint Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, Markdown, JSON]

**Output Format:** [Markdown with endpoint summaries, task status, normalized findings, and optional JSON or JSONL export references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, credit usage, task ID, terminal status, result counts, pagination coverage, failed requests, unsupported filters, and raw export location.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
