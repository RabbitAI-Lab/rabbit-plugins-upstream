## Description:

CAD tool for AI agents that helps design, model, or build 3D objects by executing build123d Python scripts and producing STEP files, PNG renders, mesh exports, and geometric metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdilla1277](https://clawhub.ai/user/jdilla1277)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to generate, inspect, compare, and iterate on local 3D CAD models from Python-based CAD scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local CAD scripts through the agentcad CLI and can create local model, render, mesh, and review artifacts.

Mitigation: Use trusted scripts and projects, review generated geometry and metrics before relying on the result, and keep CAD outputs scoped to the intended workspace.

Risk: Successful CAD runs may open local browser review artifacts by default.

Mitigation: Use --no-view for unattended, automated, or high-volume runs where browser launch would be disruptive.

Risk: Approximate comparison results are heuristic when exact 3D diffing times out.

Mitigation: Use exact diffing with an increased timeout for decisions that require precise geometric difference measurements.

## Reference(s):

- [ClawHub Agentcad Skill Listing](https://clawhub.ai/jdilla1277/skills/agentcad)
- [agentcad Documentation and Gallery](https://agentcad.dev)
- [agentcad PyPI Package](https://pypi.org/project/agentcad/)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and shell command snippets; agentcad CLI responses are JSON and generated CAD artifacts can include STEP, PNG, STL, GLB, OBJ, and HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.10-3.12 and the agentcad CLI; local browser review artifacts may open by default unless --no-view is used.]

## Skill Version(s):

0.4.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
