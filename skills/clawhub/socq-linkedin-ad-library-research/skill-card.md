## Description:

Research public Linkedin Ad Library content, accounts, keywords, and performance data with SocQ. Use when an agent needs Linkedin Ad Library-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to select SocQ Linkedin Ad Library endpoints, estimate credit use, submit and poll asynchronous collection tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid or large-volume SocQ requests may consume credits unexpectedly.

Mitigation: Report expected cost and obtain confirmation before large-volume or multi-endpoint runs.

Risk: SocQ API keys can be exposed through prompts, URLs, shell history, retained commands, or committed files.

Mitigation: Keep SOCQ_API_KEY in the environment or SocQ auth flow, and never include it in prompts, URLs, retained commands, or committed files.

Risk: Linkedin Ad Library coverage may be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report pages read, result counts, remaining cursors, unsupported filters, provider failures, and avoid claiming completeness when coverage is limited.

Risk: Retrying asynchronous submissions after timeouts can duplicate paid jobs.

Mitigation: Preserve task IDs and idempotency keys, then poll or resume the existing task instead of resubmitting blindly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-linkedin-ad-library-research)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Linkedin Ad Library API documentation](https://docs.socq.ai/api-manual/linkedin-ad-library)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Linkedin Ad Library endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown with endpoint summaries, SocQ CLI/MCP/REST command examples, task status, credit usage, and normalized findings or raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination status, credit estimates, terminal task status, unsupported filter notes, and incomplete coverage warnings.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
