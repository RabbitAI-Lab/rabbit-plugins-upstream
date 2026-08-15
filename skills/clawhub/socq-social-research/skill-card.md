## Description:

Research public social-platform content, accounts, keywords, and SEO search data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to plan and run public social-platform and SEO research through SocQ, including endpoint selection, credit estimation, asynchronous task polling, pagination, and normalized result reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends target URLs, usernames, IDs, and search queries to SocQ under the user API key.

Mitigation: Use it only for intended public social and SEO research, keep SOCQ_API_KEY in the environment, and avoid private or sensitive targets unless authorized.

Risk: Large or multi-endpoint research runs can consume paid SocQ credits.

Mitigation: Estimate costs from the capability billing data, check account limits when needed, reduce scope for uncertain inputs, and confirm broad collection before submitting.

Risk: Provider failures, unsupported filters, or early pagination stops can make coverage incomplete.

Mitigation: Report task status, failed platforms, unsupported filters, pagination limits, and collection windows so the user can judge completeness.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-social-research)
- [SocQ publisher profile](https://clawhub.ai/user/socq)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platform catalog](https://socq.ai/platforms)
- [SocQ API documentation](https://docs.socq.ai/api-manual)
- [SocQ MCP and CLI documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Capability catalog](references/catalog.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)
- [Cross-platform research](references/cross-platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint selections, command or tool-call guidance, task status summaries, and normalized research findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, credit estimates, result counts, pagination state, raw export locations, failed-platform notes, and incomplete-coverage caveats.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
