## Description:

Research public keyword volume, suggestions, related terms, difficulty, intent, organic results, and site rankings with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to select SocQ SEO endpoints, estimate credits, run public SEO data collection, poll asynchronous tasks, paginate results, and summarize normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests send user-provided domains, keywords, locales, filters, and result limits to SocQ under the configured API key.

Mitigation: Use the skill only for intended public SEO research and confirm the requested inputs before submitting them to SocQ.

Risk: The SOCQ_API_KEY could be exposed if placed in prompts, URLs, shell history, or committed files.

Mitigation: Keep SOCQ_API_KEY in the environment or configured auth store, avoid command-line API key flags during interactive use, and do not include keys in retained commands or files.

Risk: Large-volume, multi-endpoint, or dynamically priced runs can consume credits.

Mitigation: Check account limits and endpoint billing, report expected cost, reduce scope when needed, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: Results may be incomplete when pagination stops early, providers fail, filters are unsupported, or task execution has not reached a terminal state.

Mitigation: Poll asynchronous tasks to completion, preserve task IDs, follow pagination cursors until the requested cap or completion, and label incomplete coverage in the final output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-seo-research)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ SEO platform](https://socq.ai/apis/seo)
- [SocQ SEO API documentation](https://docs.socq.ai/api-manual/seo)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [SEO endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration, Markdown, Text]

**Output Format:** [Markdown or text with endpoint choices, command/API examples, task status, cost notes, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, reported credit usage, incomplete coverage notes, and failure details.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
