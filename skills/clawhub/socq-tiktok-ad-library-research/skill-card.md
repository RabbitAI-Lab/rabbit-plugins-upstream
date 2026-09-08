## Description:

Research public Tiktok Ad Library content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and analysts use this skill to select SocQ TikTok Ad Library endpoints, estimate credits, run public ad-library collection tasks, poll asynchronous jobs, paginate results, and summarize normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCQ_API_KEY with SocQ and sends selected queries, URLs, filters, and task requests to SocQ.

Mitigation: Keep the API key in the environment, avoid placing it in prompts, URLs, committed files, or retained commands, and use account-level IP, rate, and credit limits where appropriate.

Risk: SocQ requests may consume account credits, especially for large-volume or multi-endpoint runs.

Mitigation: Report expected cost, check account balance or limits, reduce scope when needed, and obtain confirmation before paid large-volume or multi-endpoint execution.

Risk: Asynchronous collection, pagination, provider failures, or unsupported filters can leave coverage incomplete.

Mitigation: Preserve task IDs, poll until a terminal state, respect pagination cursors and user-approved caps, and label incomplete coverage or mismatched filters in the final report.

Risk: Ad hoc npx execution can fetch the current CLI package at runtime.

Mitigation: Prefer a preinstalled or pinned SocQ CLI when tighter supply-chain control is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-tiktok-ad-library-research)
- [SocQ developer tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [TikTok Ad Library API documentation](https://docs.socq.ai/api-manual/tiktok-ad-library)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [TikTok Ad Library platform reference](references/platform.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with endpoint summaries, task status, normalized findings, and optional shell or API command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination status, credit estimates or reported usage, incomplete-coverage notes, and raw export locations.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
