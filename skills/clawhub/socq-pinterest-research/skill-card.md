## Description:

Research public Pinterest content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to select SocQ Pinterest endpoints, estimate credits, run asynchronous public Pinterest collections, paginate results, and summarize normalized findings or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinterest research requests and task data are sent to SocQ using a SOCQ_API_KEY.

Mitigation: Install and use the skill only when SocQ processing is intended, keep the API key in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: Large or multi-endpoint jobs can consume SocQ credits.

Mitigation: Review endpoint billing, estimate expected cost, check account limits, and obtain user confirmation before submitting paid large-volume work.

Risk: Using npx may resolve the latest @socq/cli package at runtime.

Mitigation: Pin or preinstall a reviewed @socq/cli version when supply-chain control is required.

Risk: Results may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report pages read, remaining data state, failed requests, unsupported filters, and any incomplete coverage in the final output.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Pinterest Platform](https://socq.ai/apis/pinterest)
- [SocQ Pinterest API Documentation](https://docs.socq.ai/api-manual/pinterest)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Pinterest Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint selections, command snippets, task status, and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates, pagination state, normalized findings, and raw export locations.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
