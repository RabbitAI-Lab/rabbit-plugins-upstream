## Description:

CAD tool for AI agents that designs and builds 3D objects with build123d scripts and produces CAD files, renders, mesh exports, and geometric metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdilla1277](https://clawhub.ai/user/jdilla1277)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use AgentCAD to design or revise 3D objects, inspect and validate geometry, and deliver STEP files, renders, or mesh exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Python scripts execute code to create geometry.

Mitigation: Review scripts before execution and use a dedicated Python environment.

Risk: Initialization changes project files, while builds preserve model history.

Mitigation: Use a dedicated project and inspect its configuration and history when needed.

Risk: Previews may start a local service.

Mitigation: Disable or stop the preview service when it is no longer needed.

## Reference(s):

- [AgentCAD website and gallery](https://agentcad.dev)
- [AgentCAD on PyPI](https://pypi.org/project/agentcad/)
- [AgentCAD ClawHub release](https://clawhub.ai/jdilla1277/skills/agentcad)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Files, Analysis, Guidance]

**Output Format:** [Python build123d scripts, shell commands, structured JSON, STEP files, PNG renders, STL/GLB/OBJ meshes, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Geometry outputs include validation metrics; file types depend on the requested deliverables.]

## Skill Version(s):

0.7.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
