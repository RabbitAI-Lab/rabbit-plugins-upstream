## Description:

Generates daily, weekly, monthly, or yearly reports on local agent usage, token consumption, estimated costs, tasks, and anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers analyze local WorkBuddy, Claude Code, Codex CLI, and QwenWork activity to understand usage trends and estimated costs. Reports can cover custom date ranges and be shared in Markdown, HTML, or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading local agent histories and usage databases can expose private session information.

Mitigation: Install only if you are comfortable granting access to those local records; review reports before sharing.

Risk: Optional LLM task classification sends truncated session-derived text to the configured endpoint.

Mitigation: Keep offline mode and local classification enabled for private sessions; configure an endpoint only when you accept that disclosure.

Risk: Estimated token usage and costs can differ from actual billing, especially when the source does not return token counts.

Mitigation: Treat estimates as indicative and use official usage or billing data for reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/elisabeth15501/skills/agent-analytics-report)
- [Data source and adapter documentation](docs/ADAPTERS.md)
- [Usage and privacy FAQ](references/FAQ.md)
- [Custom model pricing guide](references/add-custom-models.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, JSON]

**Output Format:** [Markdown by default; optional HTML or JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes usage trends and cost estimates; available sections vary by data source.]

## Skill Version(s):

1.9.9 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
