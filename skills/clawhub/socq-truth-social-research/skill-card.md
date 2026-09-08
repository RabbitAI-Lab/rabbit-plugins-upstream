## Description:

Research public Truth Social content, accounts, and performance data with SocQ through endpoint selection, credit estimates, asynchronous task execution, pagination, and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, analysts, and developers use this skill to collect public Truth Social profile, post, and account timeline data through SocQ. It helps agents estimate credit use, execute and poll asynchronous tasks, paginate results, and report normalized findings with coverage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends SocQ API keys and public Truth Social request inputs to a hosted third-party service.

Mitigation: Use a dedicated SOCQ_API_KEY with appropriate account controls, keep credentials in environment variables, and avoid putting keys in prompts, URLs, committed files, or retained shell commands.

Risk: SocQ requests are credit-metered, and large or multi-endpoint runs may incur cost.

Mitigation: Check expected credit usage and account limits before submission, reduce scope when needed, and obtain user confirmation before paid large-volume runs.

Risk: Public data collection can be incomplete when pagination stops early, providers fail, filters are unsupported, or requested content is unavailable.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, collection time, and any incomplete coverage.

Risk: Unpinned npx execution may fetch a moving @socq/cli version.

Mitigation: Prefer a preinstalled or pinned @socq/cli version when possible.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Truth Social API Documentation](https://docs.socq.ai/api-manual/truth-social)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Truth Social Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands, endpoint selections, task status, credit usage, normalized findings, and export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, page counts, remaining-pagination status, unsupported filters, failed requests, and incomplete coverage notes.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
