## Description:

Research public YouTube content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to select and run SocQ endpoints for public YouTube discovery, collection, comparison, and analysis. It helps estimate credits, submit asynchronous tasks, follow pagination, and report normalized results or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends YouTube research inputs to SocQ and requires a SocQ API key.

Mitigation: Install and use it only when SocQ processing is intended, keep SOCQ_API_KEY in the environment, and avoid putting keys in prompts, URLs, committed files, or retained commands.

Risk: Large or multi-endpoint SocQ jobs can consume credits.

Mitigation: Review endpoint billing, check account limits, estimate costs, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Dynamic CLI installation can introduce supply-chain uncertainty in locked-down environments.

Mitigation: Use a pinned or preinstalled @socq/cli when strict supply-chain controls are required.

Risk: Results can be incomplete if pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report task status, pages read, remaining data, failed requests, unsupported filters, and incomplete coverage.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ YouTube Platform](https://socq.ai/apis/youtube)
- [SocQ YouTube API Documentation](https://docs.socq.ai/api-manual/youtube)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [YouTube Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, task status, normalized findings, raw export locations, and inline CLI or REST commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates, page counts, coverage notes, and incomplete-result caveats.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
