## Description:

Research public Tiktok Ad Library content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, analysts, and developers use this skill to collect and analyze public Tiktok Ad Library data with SocQ while selecting appropriate endpoints, estimating credit usage, handling asynchronous tasks, and reporting pagination or coverage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ API keys can be exposed if placed in prompts, URLs, command history, or committed files.

Mitigation: Keep SOCQ_API_KEY in the environment or official CLI authentication flow and avoid embedding it in prompts, URLs, retained commands, or files.

Risk: Large or multi-endpoint research jobs can consume metered SocQ credits.

Mitigation: Review expected credit costs and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Queries and requested public ad data are sent to SocQ for collection and analysis.

Mitigation: Use the skill only when sharing the requested public ad research parameters with SocQ is acceptable.

Risk: Results can be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report pages read, remaining pagination state, failed requests, unsupported filters, and any incomplete coverage.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Tiktok Ad Library API Documentation](https://docs.socq.ai/api-manual/tiktok-ad-library)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Tiktok Ad Library Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise summaries, optional shell commands, and endpoint or task details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input summary, credit estimates, task ID, terminal status, result counts, pagination state, coverage limits, and raw export location.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
