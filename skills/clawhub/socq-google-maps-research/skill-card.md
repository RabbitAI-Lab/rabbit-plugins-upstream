## Description:

Research public Google Maps content, accounts, keywords, and performance data with SocQ through endpoint selection, credit estimation, asynchronous task execution, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public Google Maps place, review, and search data with SocQ through MCP, CLI, or REST workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to SocQ and requires a SocQ API key.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid placing keys in prompts, URLs, committed files, or retained commands, and verify authentication before submitting work.

Risk: Some SocQ requests spend credits, especially large-volume or multi-endpoint jobs.

Mitigation: Report expected cost, check account limits, reduce scope where appropriate, and obtain confirmation before paid large-volume or multi-endpoint execution.

Risk: Google Maps collection may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Preserve task IDs, report result counts and coverage limits, label unsupported filters, and avoid claiming completeness when collection is partial.

Risk: Retries can duplicate paid work or conflict with previous submissions.

Mitigation: Reuse idempotency keys after network errors, inspect normalized errors before retrying, and do not blindly resubmit failed paid requests.

## Reference(s):

- [Google Maps Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [SocQ Google Maps API Documentation](https://docs.socq.ai/api-manual/google-maps)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [SocQ Devtools Homepage](https://github.com/SocQAPI/socq-devtools)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint selections, execution commands, task status, credit details, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination state, result counts, error summaries, and cost estimates.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
