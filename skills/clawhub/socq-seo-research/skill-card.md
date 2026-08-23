## Description:

Research public keyword volume, suggestions, related terms, difficulty, intent, organic results, and site rankings with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, SEO analysts, and developers use this skill to collect public keyword and domain search data through SocQ, estimate credit costs, submit and monitor asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEO keywords, domains, and research targets are sent to SocQ through an external API.

Mitigation: Use the skill only for public SEO research and avoid sending secrets, regulated data, or confidential strategy terms.

Risk: SocQ requests are credit-metered, and large or multi-endpoint runs can consume credits quickly.

Mitigation: Estimate cost from the endpoint billing data, check account limits when needed, and require clear approval before paid large-volume or multi-endpoint runs.

Risk: The skill depends on a SocQ API key for CLI, MCP, and REST access.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid putting keys in prompts, URLs, committed files, or retained commands, and inspect authentication errors before retrying.

Risk: Asynchronous or paginated collections can be incomplete when tasks fail, polling stops early, providers fail, or filters are unsupported.

Mitigation: Preserve task IDs, poll to terminal status, follow pagination cursors, and report result counts, pages read, unsupported filters, and incomplete coverage.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ SEO Platform](https://socq.ai/apis/seo)
- [SocQ SEO API Documentation](https://docs.socq.ai/api-manual/seo)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown with endpoint choices, command or API call guidance, task status, result summaries, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include normalized SEO findings, credit usage, pagination status, incomplete coverage notes, and raw JSONL export references when available.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
