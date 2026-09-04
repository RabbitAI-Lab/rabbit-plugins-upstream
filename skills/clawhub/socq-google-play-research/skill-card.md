## Description:

Research public Google Play content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to select SocQ Google Play endpoints, estimate credits, submit and poll collection tasks, paginate results, and report normalized public Google Play findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send Google Play research inputs and a SocQ API key to SocQ's hosted service.

Mitigation: Install and use the skill only for intended SocQ workflows, keep SOCQ_API_KEY in the environment, and avoid putting credentials in prompts, URLs, committed files, or retained commands.

Risk: Unpinned npx execution can reduce repeatability for CLI-based runs.

Mitigation: Prefer a pinned or preinstalled socq CLI for repeatable execution.

Risk: Large or multi-endpoint jobs can consume paid SocQ credits.

Mitigation: Check account limits, estimate credit usage, reduce scope when needed, and confirm paid large-volume or multi-endpoint runs before submission.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Google Play API Documentation](https://docs.socq.ai/api-manual/google-play)
- [SocQ MCP and CLI Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Google Play Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint selections, command examples, task status, credit usage, pagination notes, and normalized findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, result counts, remaining-page status, and raw export locations when available.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
