## Description:

Research public Amazon content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, researchers, and analysts use this skill to select SocQ Amazon endpoints, estimate credits, run asynchronous public Amazon data collection, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to SocQ as a third-party service and requires SOCQ_API_KEY for authenticated access.

Mitigation: Install only when SocQ is approved for the intended public Amazon research workflow, store SOCQ_API_KEY securely, and avoid putting secrets or private business data in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests are credit-metered, and large or multi-endpoint jobs can create paid usage.

Mitigation: Check expected credits and account limits before submission, reduce scope when needed, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: Public Amazon collections may be incomplete when pagination stops early, provider failures occur, filters are unsupported, or date windows and locales differ.

Mitigation: Report task status, result counts, pagination state, failed requests, unsupported filters, and coverage limits instead of claiming completeness.

Risk: CLI installation through npx or @socq/cli may introduce supply-chain controls that differ by environment.

Mitigation: Use a pinned or already-installed SocQ CLI where tighter supply-chain control is required.

## Reference(s):

- [SocQ DevTools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platform page](https://socq.ai/platforms)
- [SocQ Amazon API documentation](https://docs.socq.ai/api-manual/amazon)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Amazon](references/platform.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown, Text]

**Output Format:** [Markdown or text with endpoint choices, commands or API calls, task status, credit usage, result summaries, and export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination status, unsupported filter notes, and incomplete coverage warnings.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
