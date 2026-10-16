## Description:

Guides agents through designing, editing, validating, and delivering 3D CAD models with the agentcad CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdilla1277](https://clawhub.ai/user/jdilla1277)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn 3D design requirements or existing CAD models into checked geometry and shareable CAD artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow runs generated CAD Python scripts and depends on an installed CLI.

Mitigation: Use it only where running CAD-generation Python is acceptable; prefer the ClawHub install path or pin and verify the package source.

Risk: Incorrect geometry or unchecked exports could be shared as finished work.

Mitigation: Check measurements and validation results, then review generated files and viewer output before sharing.

## Reference(s):

- [agentcad on ClawHub](https://clawhub.ai/jdilla1277/skills/agentcad)
- [agentcad documentation](https://agentcad.dev)
- [agentcad on PyPI](https://pypi.org/project/agentcad/)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Python scripts and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [AgentCAD runs can produce STEP models, PNG previews, optional STL/GLB/OBJ exports, and geometric metrics.]

## Skill Version(s):

0.7.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
