## Description:

Research public keyword volume, suggestions, related terms, difficulty, intent, organic results, and site rankings with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to collect, compare, and analyze public SEO data through SocQ. It helps select SEO endpoints, estimate credits, submit and poll asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ SEO requests send requested domains, queries, and filters to an external service and may consume credits.

Mitigation: Use the skill only for intended public SEO research, review expected costs before larger runs, and obtain user confirmation before paid large-volume or multi-endpoint execution.

Risk: The npm CLI fallback can use ad hoc npx execution and is not version-pinned.

Mitigation: Prefer an already configured MCP server or a locally installed, version-pinned @socq/cli for lower supply-chain risk.

Risk: SEO collections can be incomplete when pagination stops early, providers fail, or filters are unsupported.

Mitigation: Report result counts, pages read, unsupported filters, failed requests, and whether more data remains instead of claiming complete coverage.

## Reference(s):

- [SocQ Skill Page](https://clawhub.ai/socq/skills/socq-seo-research)
- [SocQ SEO Platform](https://socq.ai/apis/seo)
- [SocQ SEO API Documentation](https://docs.socq.ai/api-manual/seo)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SEO Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint summaries, command examples, task status, credit usage, pagination notes, and normalized SEO findings or raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, result counts, reported credit usage, collection time, incomplete coverage notes, and unsupported filter warnings.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
