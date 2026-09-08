## Description:

Research public Snapchat profiles, Spotlight items, comments, and related performance data with SocQ, including endpoint selection, credit estimates, asynchronous task handling, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external researchers use this skill to plan and run public Snapchat collection workflows through SocQ, including choosing supported endpoints, controlling cost, handling asynchronous tasks, and reporting normalized results or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Snapchat identifiers and SocQ API-authenticated requests to an external SocQ service.

Mitigation: Install and use it only for intended public Snapchat research, keep SOCQ_API_KEY in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: Ad hoc npx execution can fetch the SocQ CLI at runtime.

Mitigation: Use a pinned or preinstalled SocQ CLI when possible.

Risk: SocQ requests are credit-metered, and large or multi-endpoint runs can consume paid credits.

Mitigation: Check account balance and endpoint costs, set credit limits where available, and confirm scope before large paid runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-snapchat-research)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Snapchat API documentation](https://docs.socq.ai/api-manual/snapchat)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Snapchat endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline commands, endpoint selections, task status, result summaries, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ endpoint identifiers, expected and reported credit usage, task IDs, pagination status, collection time, and incomplete coverage notes.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
