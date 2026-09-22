## Description:

Research public Amazon content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research analysts use this skill to select and run SocQ endpoints for public Amazon product, review, seller, best-seller, and search research. It supports endpoint selection, authentication guidance, credit estimates, asynchronous task polling, pagination, normalized summaries, and raw export handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon research inputs and the SocQ API key are sent to SocQ's hosted service.

Mitigation: Install only when this hosted-service data flow is acceptable and keep SOCQ_API_KEY in the environment rather than prompts, URLs, committed files, or retained commands.

Risk: The skill can fall back to unpinned npx execution of @socq/cli.

Mitigation: Use a preinstalled or pinned @socq/cli version for stronger supply-chain control.

Risk: SocQ requests are credit-metered and larger jobs can spend credits.

Mitigation: Check expected costs, get user confirmation for paid large-volume or multi-endpoint runs, and keep SocQ credit limits enabled.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platforms](https://socq.ai/platforms)
- [SocQ Amazon API Documentation](https://docs.socq.ai/api-manual/amazon)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Amazon Platform Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, endpoint choices, task status, cost notes, result summaries, and raw export locations when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference SocQ task IDs, pagination state, credit usage, incomplete coverage, and normalized or raw JSONL output locations.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
