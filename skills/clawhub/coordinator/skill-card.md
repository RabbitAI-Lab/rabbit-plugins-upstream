## Description:

Coordinates multiple specialized agents by collecting, grouping, summarizing, and forwarding their outputs as structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to coordinate workflows that involve several role-specific agents, such as finance, technology, market, or operations reviews. It helps aggregate source-agent reports into a concise summary for a final decision maker without changing the source conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can dispatch work to multiple specialized agents, so it may involve agents the operator did not intend to include.

Mitigation: Review the agent-spawning and dispatch behavior before use and restrict coordination to the intended source agents.

Risk: Summaries can misrepresent source-agent findings if aggregation changes emphasis or omits context.

Mitigation: Keep original source-agent conclusions attached or referenced, and verify the structured summary before relying on it for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/coordinator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown reports with tables, lists, and occasional code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aggregates multiple agent outputs and preserves source-agent status, timing, and unresolved decision items.]

## Skill Version(s):

1.0.0-en2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
