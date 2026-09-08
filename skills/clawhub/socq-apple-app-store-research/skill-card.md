## Description:

Research public Apple App Store content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to select and run SocQ Apple App Store endpoints, estimate credits, submit asynchronous collection tasks, page through results, and summarize public app, review, and ranking data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an unpinned external CLI package while operating with a SocQ API key.

Mitigation: Install only when SocQ is trusted with the research inputs and API key, prefer a preinstalled or pinned @socq/cli version, and keep SOCQ_API_KEY in the environment rather than prompts, URLs, committed files, or retained commands.

Risk: Apple App Store collection is asynchronous, credit-metered, and may return incomplete coverage if pagination stops early, a provider fails, or filters are unsupported.

Mitigation: Estimate expected credits before submitting, get confirmation for paid large-volume or multi-endpoint jobs, keep task IDs for polling, inspect normalized errors before retrying, and label partial results clearly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-apple-app-store-research)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Apple App Store API documentation](https://docs.socq.ai/api-manual/apple-app-store)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Apple App Store endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint choices, command examples, task status, cost notes, result summaries, and raw export locations when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination state, reported credit usage, incomplete coverage labels, and normalized public Apple App Store findings.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
