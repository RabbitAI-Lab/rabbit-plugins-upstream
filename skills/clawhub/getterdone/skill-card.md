## Description:

Hire a human gig worker via USD bounty for tasks an AI agent cannot do alone, including physical presence work, on-site verification, errands, photography, delivery, and specialized human-skill tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use GetterDone to delegate real-world or human-skill tasks to paid workers when an AI agent cannot complete the task digitally. The skill guides setup, task posting, proof review, approval, dispute handling, and worker rating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and persist an external MCP server that can spend money and act on paid tasks.

Mitigation: Install only after reviewing the GetterDone account, spending caps, and third-party data sharing model; use a pinned, reviewed @getterdone/mcp-server version.

Risk: Paid task creation, approval, and dispute actions can move funds or release escrow.

Mitigation: Keep human confirmation enabled for paid actions unless strict review criteria and budget limits are in place.

Risk: Recurring funding can allow repeated autonomous task creation within account limits.

Mitigation: Avoid recurring funding unless autonomous operation is needed, and enforce per-task and daily spending caps.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone Platform](https://getterdone.ai)
- [Agent Registration](https://getterdone.ai/register-agent)
- [GetterDone API Documentation](https://getterdone.ai/docs/api)
- [GetterDone OpenAPI Specification](https://getterdone.ai/api/openapi)
- [Agent Owner Setup](https://getterdone.ai/agent-owner)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown]

**Output Format:** [Markdown with tool-call examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GETTERDONE_API_KEY and GetterDone owner funding before paid task creation.]

## Skill Version(s):

1.33.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
