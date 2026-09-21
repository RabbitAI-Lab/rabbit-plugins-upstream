## Description:

Research public Apple App Store content, accounts, keywords, and performance data with SocQ. Use when an agent needs Apple App Store-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to select and run SocQ Apple App Store endpoints for public app, review, ranking, keyword, account, and performance research. It supports endpoint selection, input validation, credit estimation, asynchronous task polling, pagination, and normalized or raw result reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Apple App Store research requests and SocQ API authentication to SocQ's hosted service.

Mitigation: Install only when SocQ use is intended, keep SOCQ_API_KEY in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: Requests are credit-metered and large or multi-endpoint jobs can spend credits.

Mitigation: Estimate and report expected cost, confirm large paid jobs before execution, and use account or API-key credit limits where appropriate.

Risk: Live CLI resolution through npx can change the executed package version.

Mitigation: For tighter supply-chain control, install and review a pinned version of @socq/cli.

Risk: Pagination, provider failures, unsupported filters, or early stopping can make results incomplete.

Mitigation: Report pages read, remaining data, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ Apple App Store API documentation](https://docs.socq.ai/api-manual/apple-app-store)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [Apple App Store endpoint reference](references/platform.md)
- [Authentication reference](references/authentication.md)
- [Billing and cost control reference](references/billing.md)
- [Asynchronous task reference](references/async-tasks.md)
- [Pagination and file reference](references/pagination.md)
- [Error recovery reference](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with optional shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input summary, credit usage, task status, result counts, pagination state, normalized findings, raw export location, and incomplete-coverage notes.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
