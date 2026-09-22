## Description:

Research public Google Ad Library content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to discover, collect, compare, and analyze public Google Ad Library data through SocQ endpoints. It helps select endpoints, estimate and report credits, submit asynchronous tasks, handle pagination, and summarize normalized results or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for MCP, CLI, or REST access.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid putting it in prompts, URLs, command history, or committed files, and use key limits such as IP allowlists or credit ceilings where available.

Risk: Large or multi-endpoint SocQ runs can consume credits.

Mitigation: Report expected costs, check account or endpoint billing details, reduce scope when needed, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: Results may be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Track task IDs and page counts, label incomplete coverage, preserve unsupported-filter notes, and resume polling or pagination instead of resubmitting blindly.

Risk: Using ad hoc npx execution can fetch the latest CLI package at runtime.

Mitigation: Prefer a pinned or preinstalled socq CLI when possible, as recommended by the security guidance.

## Reference(s):

- [SocQ DevTools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platforms](https://socq.ai/platforms)
- [Google Ad Library API Documentation](https://docs.socq.ai/api-manual/google-ad-library)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Async Tasks](references/async-tasks.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Errors and Recovery](references/errors.md)
- [Pagination and Files](references/pagination.md)
- [Google Ad Library](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, command guidance, task status, credit reporting, normalized findings, and export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, page counts, terminal status, credit usage, incomplete-coverage notes, and raw JSONL export locations.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
