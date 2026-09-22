## Description:

Research public Instagram content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to select SocQ Instagram endpoints, estimate credits, submit asynchronous public-data collection tasks, paginate results, and summarize normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests send public Instagram targets and queries to SocQ under the user's API key.

Mitigation: Use the skill only for intended SocQ-backed Instagram research, keep SOCQ_API_KEY in the environment, and do not place API keys in prompts, URLs, committed files, or retained commands.

Risk: Credit-metered collection can incur unintended cost during large-volume or multi-endpoint runs.

Mitigation: Check expected credits and account limits before submission, reduce scope when needed, and obtain user confirmation for paid large-volume or multi-endpoint work.

Risk: Broad follower or following collection can exceed the user's legitimate research scope.

Mitigation: Avoid broad relationship collection unless the user has a legitimate purpose and has approved a clear cap.

Risk: Pagination limits, provider failures, unsupported filters, or early stops can make results incomplete.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, and any incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-instagram-research)
- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Instagram Platform](https://socq.ai/apis/instagram)
- [SocQ Instagram API Documentation](https://docs.socq.ai/api-manual/instagram)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Instagram Platform Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Markdown with endpoint selections, command or API call guidance, task status, credit usage, result summaries, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination status, normalized result counts, failure details, and incomplete-coverage notes.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
