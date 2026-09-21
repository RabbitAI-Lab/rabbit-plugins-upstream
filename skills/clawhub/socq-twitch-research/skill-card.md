## Description:

Research public Twitch content, accounts, keywords, and performance data with SocQ for Twitch-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to collect and analyze public Twitch profile and recorded-video data through SocQ. It helps select the right endpoint, estimate credits, submit and poll asynchronous tasks, handle pagination, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocQ API key for CLI, MCP, and REST requests.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid placing it in prompts, URLs, committed files, or retained commands, and use a scoped key with rate and credit limits where possible.

Risk: SocQ requests may consume credits, especially for large or multi-endpoint runs.

Mitigation: Review the endpoint cost, account balance, and requested scope before submission, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: The workflow depends on the third-party SocQ service and the @socq/cli package.

Mitigation: Confirm trust in SocQ and the package before installation, and prefer a preinstalled or version-pinned CLI in sensitive environments.

Risk: Pagination, provider failures, unsupported filters, or early stops can make Twitch research incomplete.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, and collection time rather than claiming complete coverage.

## Reference(s):

- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Twitch API documentation](https://docs.socq.ai/api-manual/twitch)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ agent skill guide](https://docs.socq.ai/integrations/skill)
- [Twitch endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with endpoint choices, execution steps, status summaries, normalized findings, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports selected endpoint, execution path, credit usage, task ID and status, pagination coverage, unsupported filters, failures, and raw export locations when requested.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
