## Description:

Research public Pinterest content, accounts, keywords, and performance data with SocQ through Pinterest-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports using the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to select SocQ Pinterest endpoints, estimate credit use, run public Pinterest data collection, poll asynchronous tasks, paginate results, and summarize normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinterest queries, URLs, task inputs, and API-key-authorized requests are sent to SocQ.

Mitigation: Install and use the skill only when that external API use is acceptable, keep SOCQ_API_KEY in the environment, and avoid placing credentials in prompts, URLs, command history, or committed files.

Risk: Large-volume or multi-endpoint collection can spend SocQ credits.

Mitigation: Check account credit limits, report expected costs, reduce scope when appropriate, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: The npm CLI fallback may be unpinned, which can reduce reproducibility.

Mitigation: Prefer a pinned or preinstalled SocQ CLI when reproducible installs are required.

Risk: Collection may be incomplete when pagination stops early, providers fail, filters are unsupported, or tasks remain unfinished.

Mitigation: Preserve task IDs, poll until a terminal status, label incomplete coverage, and report result counts, pages read, unsupported filters, and whether more data remains.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-pinterest-research)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Pinterest Platform](https://socq.ai/apis/pinterest)
- [SocQ Pinterest API Documentation](https://docs.socq.ai/api-manual/pinterest)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Pinterest Platform Reference](references/platform.md)
- [Authentication Reference](references/authentication.md)
- [Billing and Cost Control Reference](references/billing.md)
- [Asynchronous Tasks Reference](references/async-tasks.md)
- [Pagination and Files Reference](references/pagination.md)
- [Errors and Recovery Reference](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint selections, execution commands, task status, credit usage, pagination notes, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, result counts, page counts, incomplete coverage notes, and links or paths to raw exports.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
