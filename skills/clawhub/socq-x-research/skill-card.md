## Description:

Research public X content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to select and run SocQ endpoints for public X research, estimate credit usage, manage asynchronous collection tasks, paginate results, and report normalized findings or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public X research inputs to a third-party SocQ API.

Mitigation: Submit only intended public-research inputs, keep SOCQ_API_KEY in the environment, and do not place credentials in prompts, URLs, committed files, or retained commands.

Risk: SocQ endpoint use can spend credits, especially for large-volume or multi-endpoint runs.

Mitigation: Check expected costs and account limits before submission, reduce result limits when appropriate, and obtain confirmation before large paid runs.

Risk: The skill can fall back to ad hoc npx execution for the SocQ CLI.

Mitigation: Prefer a pinned or preinstalled socq CLI when possible.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ X Platform](https://socq.ai/apis/x)
- [SocQ X API Documentation](https://docs.socq.ai/api-manual/x)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [X Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Configuration]

**Output Format:** [Markdown guidance with inline CLI, MCP, and REST examples plus normalized result summaries or raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, credit estimate, task ID, terminal status, result count, pagination status, collection time, and incomplete-coverage notes.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
