## Description:

Research public Reddit content, accounts, keywords, and performance data with SocQ. Use when an agent needs Reddit-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to select and run SocQ endpoints for public Reddit research, including endpoint choice, cost estimation, asynchronous task handling, pagination, and normalized reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public Reddit research inputs and a SocQ API key to SocQ's hosted service.

Mitigation: Use SOCQ_API_KEY through the environment, avoid putting keys in prompts, URLs, committed files, or retained commands, and apply API-key limits where available.

Risk: Large-volume or multi-endpoint runs can spend SocQ credits.

Mitigation: Check account balance and endpoint billing, estimate expected cost, reduce requested scope when needed, and obtain user confirmation before paid large-volume work.

Risk: Research output can be incomplete when pagination stops early, providers fail, or requested filters are unsupported.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, and any incomplete coverage instead of claiming completeness.

Risk: Floating npx execution can install a newer CLI than the reviewer expected.

Mitigation: For stricter environments, preinstall or pin @socq/cli before using the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-reddit-research)
- [SocQ Devtools Homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Reddit API Documentation](https://docs.socq.ai/api-manual/reddit)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Asynchronous Tasks](references/async-tasks.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Errors and Recovery](references/errors.md)
- [Pagination and Files](references/pagination.md)
- [Reddit Endpoint Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint summaries, execution paths, cost information, task status, pagination notes, normalized findings, and optional raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, result counts, pages read, credit estimates or usage, failed requests, unsupported filters, and incomplete-coverage notes.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
