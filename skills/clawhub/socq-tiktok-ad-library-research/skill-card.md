## Description:

Research public Tiktok Ad Library content, accounts, keywords, and performance data with SocQ. Use when an agent needs Tiktok Ad Library-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to collect and analyze public TikTok Ad Library records through SocQ endpoints, including endpoint selection, credit estimates, asynchronous task polling, pagination, and normalized reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and public-ad targets are sent to SocQ during normal use.

Mitigation: Install only when SocQ is an intended processor for the research workflow and avoid submitting sensitive or out-of-scope information.

Risk: The skill can incur SocQ credit usage, especially for large-volume or multi-endpoint collection.

Mitigation: Review the expected cost, account balance, and endpoint billing details before starting large paid runs.

Risk: A floating npx invocation can install a newer @socq/cli than the operator has reviewed.

Mitigation: Prefer a pinned or preinstalled @socq/cli and keep SOCQ_API_KEY scoped and rate-limited where possible.

Risk: Pagination stops, provider failures, unsupported filters, or incomplete tasks can make results incomplete.

Mitigation: Report task status, pages read, unsupported filters, failed requests, and whether more data remains instead of claiming complete coverage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-tiktok-ad-library-research)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ TikTok Ad Library API Documentation](https://docs.socq.ai/api-manual/tiktok-ad-library)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Platform Reference](references/platform.md)
- [Authentication Reference](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, JSON, guidance]

**Output Format:** [Markdown responses with endpoint summaries, command or API examples, task status, pagination notes, and normalized findings or raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes expected and reported credit usage when available, task IDs, terminal status, result counts, pages read, and incomplete-coverage notes.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
