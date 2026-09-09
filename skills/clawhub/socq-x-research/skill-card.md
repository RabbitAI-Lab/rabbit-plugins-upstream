## Description:

Research public X content, accounts, keywords, and performance data with SocQ through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to plan, collect, and analyze public X posts, profiles, trends, replies, quotes, repost relationships, followers, and following data through SocQ. It helps select endpoints, estimate credits, submit asynchronous tasks, handle pagination, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, usernames, post URLs, and related parameters are sent to SocQ for public X research.

Mitigation: Use this skill only for intended public X research and avoid submitting sensitive or unnecessary parameters.

Risk: SocQ requests are credit-metered and large or multi-endpoint jobs can incur higher costs.

Mitigation: Check account limits, estimate credits, reduce result limits when appropriate, and confirm scope before large paid collection jobs.

Risk: Ad hoc npx execution can introduce package supply-chain uncertainty.

Mitigation: Prefer a pinned or preinstalled @socq/cli version when CLI execution is needed.

## Reference(s):

- [SocQ Skill Page](https://clawhub.ai/socq/skills/socq-x-research)
- [SocQ CLI Homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ X Platform](https://socq.ai/apis/x)
- [SocQ X API Documentation](https://docs.socq.ai/api-manual/x)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [X Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown reports with endpoint choices, command or API details, and JSON task or result summaries when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input summary, expected and reported credit usage, task ID, terminal status, result counts, pagination status, collection time, incomplete coverage notes, and raw export locations.]

## Skill Version(s):

1.0.3 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
