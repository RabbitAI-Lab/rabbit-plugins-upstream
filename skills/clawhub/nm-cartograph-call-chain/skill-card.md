## Description:

Traces execution paths through the code graph with criticality scoring and Mermaid charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to trace how functions and entry points propagate through a codebase, inspect call paths, and summarize criticality factors such as file spread, security sensitivity, external calls, test gaps, and depth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run repository search commands or a local graph query helper to inspect call chains.

Mitigation: Install it only for agents that should inspect the local codebase, and review command output before acting on criticality assessments.

Risk: Missing gauntlet graph data can limit flow tracing to static text-search results.

Mitigation: Use the documented fallback search path when graph data is unavailable, or build the graph before relying on graph-specific analysis.

## Reference(s):

- [Cartograph plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shell command snippets, indented call trees, Mermaid flowcharts, and criticality summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on a local gauntlet graph query helper; falls back to text search when graph data is unavailable.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
