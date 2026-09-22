## Description:

Research public social-platform content, accounts, keywords, and SEO search data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to discover SocQ endpoints, estimate credit cost, submit and poll asynchronous jobs, paginate results, and summarize public social-platform and SEO data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, URLs, usernames, platform IDs, and other public-data targets are sent to SocQ.

Mitigation: Install and use the skill only when this data sharing is acceptable for the intended workflow.

Risk: SocQ requests are credit-metered, and large or multi-platform jobs can incur unexpected cost.

Mitigation: Check account balance and endpoint billing, reduce scope when appropriate, and confirm expected spend before large runs.

Risk: Runtime package resolution with npx can introduce supply-chain variability.

Mitigation: Prefer pinned or preinstalled SocQ CLI/MCP packages in managed environments.

Risk: Provider failures, unsupported filters, early pagination stops, or differing collection windows can make coverage incomplete or comparisons misleading.

Mitigation: Report collection windows, filters, result counts, failed platforms, pagination state, and any unsupported parameters with the findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-social-research)
- [SocQ developer tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platform catalog](https://socq.ai/platforms)
- [SocQ API documentation](https://docs.socq.ai/api-manual)
- [SocQ MCP and CLI documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Capability catalog](references/catalog.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Cross-platform research](references/cross-platform.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint selections, concise execution summaries, inline shell commands when useful, and normalized findings or raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include requested platforms, filters, credit estimates and usage, task IDs, terminal statuses, result counts, pagination state, failed platforms, and incomplete coverage notes.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
