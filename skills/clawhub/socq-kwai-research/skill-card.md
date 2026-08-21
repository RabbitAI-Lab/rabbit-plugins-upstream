## Description:

Research public Kwai content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to select SocQ Kwai endpoints, collect public Kwai posts or profiles, handle asynchronous tasks and pagination, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocQ API key for MCP, CLI, and REST requests.

Mitigation: Store SOCQ_API_KEY in the environment or SocQ CLI config, avoid putting keys in prompts or URLs, and confirm the installation posture before use.

Risk: SocQ requests can spend credits, especially for large-volume or multi-endpoint collection.

Mitigation: Review credit estimates, account limits, and request scope before approving paid large-volume or multi-endpoint runs.

Risk: Asynchronous collection, pagination stops, provider failures, or unsupported filters can produce incomplete coverage.

Mitigation: Track task IDs, poll to terminal status, report pages read and whether more data remains, and label incomplete or unsupported coverage in the final output.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platform page](https://socq.ai/platforms)
- [Kwai API documentation](https://docs.socq.ai/api-manual/kwai)
- [SocQ MCP and CLI overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Kwai endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint choices, execution commands or API call guidance, status summaries, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates or usage, page counts, incomplete-coverage notes, and error summaries.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
