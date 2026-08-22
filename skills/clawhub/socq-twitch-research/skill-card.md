## Description:

Research public Twitch content, accounts, keywords, and performance data with SocQ through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to select SocQ Twitch endpoints, estimate credits, submit public Twitch research tasks, poll asynchronous results, paginate responses, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Large-volume or multi-endpoint SocQ jobs can consume paid credits.

Mitigation: Estimate expected credits and obtain user confirmation before starting larger paid runs.

Risk: SOCQ_API_KEY exposure could allow unauthorized SocQ API use.

Mitigation: Keep the key in the environment or approved local config, and avoid prompts, URLs, command history, and committed files.

Risk: Public Twitch research can be incomplete if pagination stops early, providers fail, or filters are unsupported.

Mitigation: Report task status, pages read, remaining data, failed requests, unsupported filters, and collection time with the findings.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Platform Overview](https://socq.ai/platforms)
- [SocQ Twitch API Documentation](https://docs.socq.ai/api-manual/twitch)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Twitch Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint choices, input summaries, credit notes, task status, normalized findings, and optional raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCQ_API_KEY; large-volume or multi-endpoint paid runs should include a cost estimate and user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
