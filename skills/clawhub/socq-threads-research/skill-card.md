## Description:

Research public Threads content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to select SocQ Threads endpoints, collect public Threads data, estimate credit usage, manage asynchronous tasks, paginate results, and return normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public Threads research inputs and task requests are sent to the external SocQ service.

Mitigation: Use the skill only for intended public Threads collection, keep SOCQ_API_KEY in the environment, and avoid putting credentials or private data in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests are credit-metered and large or multi-endpoint runs can consume credits.

Mitigation: Check expected costs and account limits, reduce result limits when appropriate, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: Ad-hoc npx execution can introduce package-version drift.

Mitigation: Prefer a pinned or already installed socq CLI for repeatable execution.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Threads platform](https://socq.ai/apis/threads)
- [SocQ Threads API documentation](https://docs.socq.ai/api-manual/threads)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Threads platform reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise summaries, endpoint selections, task status, normalized findings, raw export locations, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input filters, expected and reported credit usage, task ID, terminal status, result counts, pagination state, collection time, and coverage limits.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
