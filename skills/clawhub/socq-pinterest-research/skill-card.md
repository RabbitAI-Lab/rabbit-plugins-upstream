## Description:

Research public Pinterest content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to select and run SocQ endpoints for public Pinterest discovery, collection, comparison, and analysis. It supports endpoint selection, input validation, credit estimates, asynchronous task handling, pagination, and normalized reporting through SocQ MCP, CLI, or REST workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests can spend account credits, especially for large-volume or multi-endpoint Pinterest research.

Mitigation: Review expected costs, account limits, and requested scope before execution, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: The skill requires a SocQ API key for CLI, MCP, and REST requests.

Mitigation: Use a scoped SOCQ_API_KEY where possible and keep credentials out of prompts, URLs, shell history, retained commands, and committed files.

Risk: Pinterest collection may be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report pagination status, provider failures, unsupported filters, collection time, and incomplete coverage instead of claiming complete results.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Pinterest Platform](https://socq.ai/apis/pinterest)
- [SocQ Pinterest API Documentation](https://docs.socq.ai/api-manual/pinterest)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Pinterest Endpoint Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Configuration instructions, Markdown, Files]

**Output Format:** [Markdown with endpoint summaries, task status, credit usage, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include task IDs, pagination status, result counts, incomplete coverage notes, and file locations for raw JSONL exports.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
