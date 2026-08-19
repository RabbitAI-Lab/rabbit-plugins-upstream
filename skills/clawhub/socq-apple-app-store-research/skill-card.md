## Description:

Research public Apple App Store app details, reviews, rankings, keywords, and performance data with SocQ through MCP, CLI, or REST workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to collect, compare, and analyze public Apple App Store app details, reviews, and rankings with SocQ. It helps select endpoints, estimate and report credit usage, run asynchronous tasks, handle pagination, and summarize normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocQ API key and sends Apple App Store research inputs to SocQ.

Mitigation: Confirm this data flow is acceptable before installation, keep SOCQ_API_KEY in the environment, and do not place keys in prompts, URLs, committed files, or retained commands.

Risk: Large or multi-endpoint research jobs can consume paid SocQ credits.

Mitigation: Report expected credits, check account or key limits when needed, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Results may be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Preserve task IDs and pagination state, inspect normalized errors before retrying, and label incomplete coverage or unsupported filters in the final output.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Apple App Store API Documentation](https://docs.socq.ai/api-manual/apple-app-store)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Apple App Store Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, command or API examples, task status, credit usage, normalized findings, and raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected SocQ endpoint, execution path, input summary, task ID, pagination status, expected and reported credits, failed requests, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
