## Description:

Research public Kwai content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to select and run SocQ endpoints for public Kwai posts, profiles, user posts, pagination, task polling, and normalized result reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested Kwai identifiers, queries, task requests, and SocQ API authentication to SocQ services.

Mitigation: Use the skill only for intended public Kwai research, keep SOCQ_API_KEY in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests are credit-metered, and larger or multi-endpoint runs may incur unexpected cost.

Mitigation: Review endpoint credit estimates, account limits, and expected result volume before approving paid or large-volume collection.

Risk: Ad hoc npx execution may install or run the current CLI package at execution time.

Mitigation: Prefer a pinned or preinstalled socq CLI when possible.

Risk: Pagination, provider errors, unsupported filters, or early task termination can make results incomplete.

Mitigation: Track task IDs and pagination cursors, inspect normalized errors before retrying, and label incomplete coverage in user-facing results.

## Reference(s):

- [SocQ Agent Card](https://clawhub.ai/socq/skills/socq-kwai-research)
- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platforms](https://socq.ai/platforms)
- [SocQ Kwai API Documentation](https://docs.socq.ai/api-manual/kwai)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Kwai Endpoint Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, command examples, task status, credit usage, and normalized findings or export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, incomplete-coverage notes, and links or paths to raw JSONL exports when available.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
