## Description:

Research public Rednote content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and run public Rednote research through SocQ, including endpoint selection, credit estimates, asynchronous task polling, pagination, normalized analysis, and raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rednote research queries, supplied URLs, and collection parameters are sent to SocQ's hosted service using SOCQ_API_KEY.

Mitigation: Use a scoped API key with rate, IP, or credit limits, keep the key in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests are credit-metered and larger jobs can consume paid credits.

Mitigation: Estimate endpoint costs, check account limits, reduce scope where practical, and obtain confirmation before large-volume or multi-endpoint runs.

Risk: Using unpinned npx or CLI installation paths can add normal supply-chain exposure.

Mitigation: Prefer a pinned or already-installed SocQ CLI when stricter supply-chain control is required.

Risk: Pagination limits, provider failures, unsupported filters, or early stops can make research coverage incomplete.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, and any partial collection boundaries in the final output.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platforms](https://socq.ai/platforms)
- [Rednote API Documentation](https://docs.socq.ai/api-manual/rednote)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Platform Reference](references/platform.md)
- [Authentication Reference](references/authentication.md)
- [Billing Reference](references/billing.md)
- [Asynchronous Tasks Reference](references/async-tasks.md)
- [Pagination Reference](references/pagination.md)
- [Errors Reference](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, task status, result counts, normalized findings, raw export locations, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes expected and reported credit usage when available, pagination state, collection time, failures, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
