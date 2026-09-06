## Description:

Research public Google Ad Library content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to select SocQ Google Ad Library endpoints, estimate credit usage, run public ad-library collection workflows, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCQ_API_KEY for authenticated SocQ API, CLI, MCP, or REST requests.

Mitigation: Keep the key in the process environment, avoid putting it in prompts, URLs, command history, committed files, or retained commands, and use API-key IP, rate, or credit limits where available.

Risk: The integration can run the SocQ CLI, including ad hoc npx execution, without a pinned version.

Mitigation: Prefer an already configured MCP server or a pinned, preinstalled CLI before using ad hoc npx execution.

Risk: SocQ requests are credit-metered, and large or multi-endpoint collections can spend credits.

Mitigation: Review expected cost and scope before paid large-volume runs, check account limits, and reduce result limits or endpoint count when the user has not approved a larger spend.

Risk: Results can be incomplete when pagination stops early, provider failures occur, or filters are unsupported.

Mitigation: Report pagination status, failed requests, unsupported filters, collection time, and incomplete coverage rather than claiming completeness.

## Reference(s):

- [SocQ Skill Page](https://clawhub.ai/socq/skills/socq-google-ad-library-research)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platform Page](https://socq.ai/platforms)
- [Google Ad Library API Documentation](https://docs.socq.ai/api-manual/google-ad-library)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Google Ad Library Platform Reference](artifact/references/platform.md)
- [Authentication Reference](artifact/references/authentication.md)
- [Billing and Cost Control Reference](artifact/references/billing.md)
- [Asynchronous Tasks Reference](artifact/references/async-tasks.md)
- [Pagination and Files Reference](artifact/references/pagination.md)
- [Errors and Recovery Reference](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured text with CLI, MCP, or REST execution details and normalized result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include endpoint selection, input and filter summaries, credit estimates, task IDs, terminal status, pagination coverage, normalized findings, and raw export locations.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
