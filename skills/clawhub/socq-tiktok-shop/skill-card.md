## Description:

Research public TikTok Shop products, shops, creators, categories, and sales signals with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to select SocQ TikTok Shop endpoints, estimate credits, run authenticated MCP, CLI, or REST collections, poll asynchronous tasks, paginate results, and report normalized public TikTok Shop research findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated SocQ requests send queries, product or shop URLs, and related request data to SocQ under the user's API key.

Mitigation: Install and use the skill only for intended TikTok Shop research, keep SOCQ_API_KEY in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests are credit-metered, and large or multi-endpoint runs can spend credits.

Mitigation: Check expected endpoint costs, set credit limits when available, and require user confirmation before paid large-volume or multi-endpoint runs.

Risk: Results can be incomplete when pagination stops early, providers fail, filters are unsupported, or collection windows differ.

Mitigation: Report task status, pages read, remaining pagination, failed requests, unsupported filters, collection time, and any incomplete coverage or comparison limits.

Risk: Installing the SocQ CLI introduces a third-party executable dependency.

Mitigation: Use a preinstalled trusted socq binary or pin @socq/cli to a reviewed version before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-tiktok-shop)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ TikTok Shop API](https://socq.ai/apis/tiktok-shop)
- [SocQ TikTok Shop API Documentation](https://docs.socq.ai/api-manual/tiktok-shop)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [TikTok Shop Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint selections, command examples, task status summaries, credit estimates, normalized findings, and raw export locations when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, result counts, incomplete-coverage notes, failed-request summaries, and unsupported-filter notes.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
