## Description:

Research public Facebook content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to select SocQ Facebook endpoints, estimate paid API credits, run asynchronous public Facebook data collection through MCP, CLI, or REST, and summarize normalized results or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests send public Facebook research queries and API-authenticated requests to a third-party service.

Mitigation: Install and use the skill only when that data flow is intended, keep SOCQ_API_KEY in the environment, and avoid placing keys in prompts, URLs, committed files, or retained commands.

Risk: Facebook collections are credit-metered and large or repeated jobs can consume paid credits.

Mitigation: Inspect endpoint billing, check account limits, reduce requested result limits when needed, and get user confirmation before paid large-volume or multi-endpoint runs.

Risk: Bulk collection or raw export of social-media data can create authorization, privacy, and completeness concerns.

Mitigation: Collect only public data supported by the selected endpoint, get appropriate authorization before bulk collection or raw export, and label incomplete coverage when pagination stops early, a provider fails, or a filter is unsupported.

Risk: Unpinned npx execution can install a changing CLI package at runtime.

Mitigation: Prefer a pinned or preinstalled SocQ CLI for repeat use.

## Reference(s):

- [SocQ Devtools Homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Facebook Platform](https://socq.ai/apis/facebook)
- [SocQ Facebook API Documentation](https://docs.socq.ai/api-manual/facebook)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Facebook Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown or text summaries with endpoint IDs, input and filter summaries, credit estimates, task status, result counts, normalized findings, and optional raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCQ_API_KEY; SocQ requests are asynchronous, credit-metered, and scoped to public Facebook data supported by selected endpoints.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
