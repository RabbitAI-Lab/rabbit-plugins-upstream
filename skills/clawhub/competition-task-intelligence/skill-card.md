## Description:

Build and maintain a structured PDE equation registry, analyze competition tasks (difficulty, bottlenecks, score projections), generate strategic recommendations for research focus, and expose this intelligence via CLI and MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research engineers use this skill to organize PDE equation metadata, analyze competition task difficulty and score potential, and choose research focus through CLI and MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned expflow-pde package as an MCP server can expose an unclear tool surface to the agent environment.

Mitigation: Pin expflow-pde to a trusted exact version, inspect the package source, and verify the available MCP tools before connecting the server.

Risk: MCP tools may interact with credentials, datasets, ClearML, Langfuse, workers, or GPU-backed execution paths.

Mitigation: Run the server with least-privilege credentials, avoid broad environment access, and confirm what each tool can read or change before deployment.

Risk: Competition task metadata, hardcoded scores, deadlines, or duplicated scoring formulae may become stale and mislead planning decisions.

Mitigation: Review task metadata, deadlines, scores, and scoring formulae against current competition records before relying on recommendations.

Risk: Experiment runs can incur hardware, worker, storage, or GPU costs.

Mitigation: Quote costs only from recorded runs and limit worker or GPU access until the workflow has been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/diamond2nv/skills/competition-task-intelligence)
- [Project homepage](https://github.com/diamond2nv/expflow)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks, shell commands, configuration snippets, and structured analysis guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PDE registry summaries, task analysis, score projections, strategic recommendations, CLI examples, MCP configuration, and risk-aware installation guidance.]

## Skill Version(s):

0.7.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
