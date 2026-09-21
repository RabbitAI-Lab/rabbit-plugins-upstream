## Description:

Research public LinkedIn content, accounts, keywords, and performance data with SocQ endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public LinkedIn company, profile, job, post, comment, and search data through SocQ while tracking endpoint choice, costs, task status, pagination, and coverage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested public LinkedIn queries and API-authenticated requests to SocQ.

Mitigation: Use the skill only when SocQ is an approved provider for the requested research, keep SOCQ_API_KEY in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: Large or broad collections can consume paid SocQ credits.

Mitigation: Check account balance and endpoint billing before submission, reduce result limits when appropriate, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Results can be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, and any incomplete coverage instead of claiming completeness.

Risk: Installing the SocQ CLI without version controls can pull a newer package than expected.

Mitigation: Prefer a vetted or pinned @socq/cli version where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-linkedin-research)
- [SocQ developer tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ LinkedIn APIs](https://socq.ai/apis/linkedin)
- [SocQ LinkedIn API documentation](https://docs.socq.ai/api-manual/linkedin)
- [SocQ MCP and CLI integration overview](https://docs.socq.ai/integrations/overview)
- [SocQ agent skill guide](https://docs.socq.ai/integrations/skill)
- [LinkedIn endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI, MCP, or REST commands and normalized result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include endpoint selection, input and filter summaries, expected and reported credit usage, task IDs, terminal task status, page counts, coverage limits, normalized findings, or raw export locations.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
