## Description:

Create, edit, verify and export parametric FreeCAD models (STEP, STL, 3MF) and DXF drawings from JSON; STL import; stress checks; optional parts from GitHub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninja7v](https://clawhub.ai/user/ninja7v)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use the skill to create and edit parametric FreeCAD models from JSON requests, check geometry, and export CAD files or DXF drawings. It can also import STL meshes and run linear static stress checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had partial coverage: 48 of 49 components were fully inspected, and some obfuscated instruction text and references could not be fully evaluated.

Mitigation: Review the remaining coverage and reported alerts before installing or enabling the skill.

Risk: Finding or importing optional FreeCAD library parts can make anonymous requests to GitHub.

Mitigation: Set FCSKILL_OFFLINE=1 to forbid network access, or use a local library clone through FCSKILL_LIBRARY.

Risk: A stress result can be unverified when equilibrium or mesh convergence checks are unavailable; the analysis is a linear static estimate.

Mitigation: Check the reported equilibrium and convergence statuses, treat unavailable checks as unverified, and do not treat the estimate as a certified calculation.

## Reference(s):

- [FreeCAD skill release on ClawHub](https://clawhub.ai/ninja7v/skills/freecad-skill)

## Skill Output:

**Output Type(s):** [Files, JSON, Analysis]

**Output Format:** [Native FreeCAD documents and exported CAD files (STEP, STL, 3MF and other supported formats), DXF drawings, and JSON operation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model dimensions use millimetres and degrees; stress checks are linear static estimates.]

## Skill Version(s):

2.0.3 (source: frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
