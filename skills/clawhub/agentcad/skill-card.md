## Description:

CAD tool for AI agents that helps design, model, and build 3D objects by executing build123d Python scripts and producing CAD artifacts and geometric metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdilla1277](https://clawhub.ai/user/jdilla1277)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create and iterate on CAD models, inspect generated geometry, export mesh formats, and validate measurable design requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a local external CAD CLI that runs Python CAD scripts and creates project output files.

Mitigation: Install agentcad only from trusted package sources, prefer pinned versions where supply-chain controls require them, and review generated scripts before execution.

Risk: Generated CAD geometry or approximate diff metrics can be incorrect or incomplete if scripts, constraints, or comparisons are wrong.

Mitigation: Use dry runs, previews, inspection, measurement, and explicit spec checks before relying on generated CAD artifacts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jdilla1277/skills/agentcad)
- [agentcad Documentation and Gallery](https://agentcad.dev)
- [agentcad CLI Source](https://github.com/jdilla1277/agentcad)
- [agentcad PyPI Package](https://pypi.org/project/agentcad/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands, Python CAD script examples, and JSON response interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agentcad CLI may create STEP files, PNG renders, STL/GLB/OBJ exports, viewer HTML, diffs, and metrics in project output directories.]

## Skill Version(s):

0.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
