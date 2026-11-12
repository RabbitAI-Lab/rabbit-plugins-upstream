## Description:

Create, edit, verify and export parametric FreeCAD models (STEP, STL, 3MF) and DXF drawings from JSON; STL import; mass and stress checks; parts from GitHub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninja7v](https://clawhub.ai/user/ninja7v)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and mechanical engineers use this skill to create and revise FreeCAD models, inspect dimensions and mass properties, run linear static stress checks, and export parts or DXF drawings from JSON requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marked this release suspicious and partial, including a concern that a geometry check may report an unverified result as clean.

Mitigation: Review the geometry-check behavior and inspect critical models in FreeCAD before relying on a clean result.

## Reference(s):

- [FreeCAD skill release](https://clawhub.ai/ninja7v/skills/freecad-skill)
- [FreeCAD parts library](https://github.com/FreeCAD/FreeCAD-library)

## Skill Output:

**Output Type(s):** [Files, Analysis, Guidance]

**Output Format:** [Parametric FreeCAD documents, STEP/STL/3MF exports, DXF drawings, and JSON operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model dimensions use millimetres and degrees; operation results include geometry and export checks. Stress analysis is linear static.]

## Skill Version(s):

3.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
