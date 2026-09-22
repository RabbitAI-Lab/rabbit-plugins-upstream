## Description:

Research public Facebook content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, analysts, and developers use this skill to select SocQ Facebook endpoints, estimate credit costs, run authorized public Facebook data collection, and report normalized findings or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facebook research inputs, task results, and API credentials are handled by SocQ services.

Mitigation: Confirm trust in SocQ before installation, keep SOCQ_API_KEY scoped and rate-limited where possible, and never place keys in prompts, URLs, committed files, or retained commands.

Risk: Large or multi-endpoint jobs can consume credits unexpectedly.

Mitigation: Inspect endpoint billing, check account balance, reduce scope when needed, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Live npx execution can fetch the current CLI package at runtime.

Mitigation: Prefer a pinned or preinstalled SocQ CLI when operational stability or supply-chain control matters.

Risk: Collection can be incomplete when pagination stops early, a provider fails, or filters are unsupported.

Mitigation: Report task status, pages read, result counts, failed requests, unsupported filters, and any incomplete coverage instead of claiming completeness.

Risk: Use outside authorized public-data research may create compliance issues.

Mitigation: Use the skill only for authorized, compliant collection of public Facebook data supported by the selected endpoint.

## Reference(s):

- [SocQ Facebook API Documentation](https://docs.socq.ai/api-manual/facebook)
- [SocQ Facebook Platform](https://socq.ai/apis/facebook)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [Facebook Endpoint Reference](references/platform.md)
- [Authentication Reference](references/authentication.md)
- [Billing and Cost Control Reference](references/billing.md)
- [Asynchronous Task Reference](references/async-tasks.md)
- [Pagination and Files Reference](references/pagination.md)
- [Errors and Recovery Reference](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline commands and structured status details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include endpoint choice, execution path, credit usage, task status, result counts, pagination status, normalized findings, and raw export location.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
