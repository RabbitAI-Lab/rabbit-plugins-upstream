## Description:

Generates a Mermaid dependency graph showing import relationships between modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect codebase import relationships, understand coupling, find circular dependencies, and plan refactors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks the agent to inspect imports and dependency structure, which may expose sensitive repository architecture when used on private codebases.

Mitigation: Use explicit scopes and avoid running the workflow over sensitive paths unless that repository inspection is intended.

Risk: Graph rendering may send Mermaid graph content to a Mermaid MCP service.

Mitigation: Review the generated graph content before rendering when working with confidential module names or dependency structures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-dependency-graph)
- [Cartograph source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Code, API Calls, Guidance]

**Output Format:** [Markdown with Mermaid flowchart code and analysis notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a rendered Mermaid diagram when the configured Mermaid MCP service is available.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
