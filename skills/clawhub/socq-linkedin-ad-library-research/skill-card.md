## Description:

Research public Linkedin Ad Library content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to select SocQ Linkedin Ad Library endpoints, estimate credit usage, run public ad-library collection, poll asynchronous tasks, page through results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents need access to a SocQ API key to use the hosted tools, CLI, or REST API.

Mitigation: Keep SOCQ_API_KEY in the process environment, avoid putting keys in prompts, URLs, command history, committed files, or retained commands, and configure key limits where appropriate.

Risk: SocQ requests are credit-metered, and large or multi-endpoint collection can incur cost.

Mitigation: Report expected credit usage, check account or endpoint billing details, reduce scope when needed, and require confirmation before broad or paid collection runs.

Risk: Asynchronous tasks, pagination stops, provider failures, or unsupported filters can leave coverage incomplete.

Mitigation: Poll tasks to a terminal status, preserve task IDs, follow pagination cursors until the approved cap or completion, and label incomplete coverage or unsupported filters in the final response.

Risk: Blind retries can duplicate paid requests or conflict with idempotency controls.

Mitigation: Inspect normalized errors before retrying, reuse idempotency keys after network failures, and avoid resubmitting failed paid tasks without user approval.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platforms](https://socq.ai/platforms)
- [Linkedin Ad Library API Documentation](https://docs.socq.ai/api-manual/linkedin-ad-library)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Linkedin Ad Library](references/platform.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown with endpoint selections, command examples, task status, credit reporting, result summaries, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination status, reported credit usage, incomplete coverage notes, and normalized public Linkedin Ad Library findings.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
