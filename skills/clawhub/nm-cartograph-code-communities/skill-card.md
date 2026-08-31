## Description:

Detects architectural clusters and coupling boundaries via community detection on the code graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to identify module groupings, coupling boundaries, and refactoring targets in a codebase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use an already-installed gauntlet plugin to inspect repository graph data.

Mitigation: Use only trusted gauntlet/plugin installations and review what plugin code will run before relying on graph-backed output.

Risk: Fallback analysis based on directories and imports can approximate module boundaries and coupling.

Mitigation: Treat clusters, warnings, and refactoring suggestions as review inputs and confirm them against the codebase before making architectural changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-code-communities)
- [Cartograph homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with analysis tables, Mermaid diagrams, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use gauntlet graph data when available; otherwise falls back to directory and import analysis.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
