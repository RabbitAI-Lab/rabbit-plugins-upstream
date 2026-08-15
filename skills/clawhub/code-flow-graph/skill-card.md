## Description:

Generate interactive HTML node-graph diagrams for code visualization, including architecture overviews, module dependencies, call chains, class relationships, UI event flows, and widget hierarchy layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[biubiubiu533](https://clawhub.ai/user/biubiubiu533)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to analyze a codebase and produce interactive diagrams that explain module structure, entry-point call chains, UI flows, data types, and implementation relationships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The validator executes code_flow_graph_data.js as JavaScript.

Mitigation: Use the validator only with generated or trusted diagram data, and review or replace it before validating untrusted files.

Risk: The skill reads the target project, writes diagram files, and stores persistent session metadata.

Mitigation: Run it only in intended workspaces and review generated diagram and state files before committing or sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/biubiubiu533/skills/code-flow-graph)
- [Server-resolved source repository](https://github.com/biubiubiu533/Code_Flow_Graph)
- [Server-resolved source commit](https://github.com/biubiubiu533/Code_Flow_Graph/tree/20d33c52573d210f774a3141ab088f3f73f37928)
- [Analysis guide](references/analysis_guide.md)
- [Data format reference](references/data_format.md)
- [Deep-dive diagram types](references/deep_dive_types.md)
- [AuroraView example repository](https://github.com/loonghao/auroraview)
- [Catppuccin palette](https://github.com/catppuccin/catppuccin)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated HTML and JavaScript files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a standalone HTML viewer, a JavaScript diagram data file, and local session metadata for incremental diagram updates.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
