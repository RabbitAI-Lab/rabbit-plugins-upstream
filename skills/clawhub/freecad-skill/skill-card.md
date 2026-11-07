## Description:

Create, edit, verify and export parametric FreeCAD models (FCStd, STEP, STL, 3MF) from JSON: parts, enclosures, brackets, 3D prints, dimension changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninja7v](https://clawhub.ai/user/ninja7v)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers can use JSON requests to create and edit parametric FreeCAD parts and assemblies, inspect geometry, check fits or estimated strength, and export CAD and drawing files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional Python operation can run agent-written code with access beyond the modeling workspace.

Mitigation: Keep FCSKILL_ALLOW_PYTHON disabled unless running trusted code with the intended account access.

Risk: Searching for and importing library parts can download files from GitHub.

Mitigation: Set FCSKILL_OFFLINE=1 to prevent network access, or use a local FreeCAD parts-library clone.

Risk: Editing CAD documents can damage work if a model change has unintended results.

Mitigation: Use a dedicated modeling folder and keep backups of files being edited.

Risk: Static stress-analysis estimates may be incomplete or unreliable when warnings, equilibrium, or convergence results are not checked.

Mitigation: Review warnings and confirm equilibrium and convergence results before relying on estimates; do not treat them as certified calculations.

## Reference(s):

- [Operations reference](docs/OPERATIONS.md)
- [FreeCAD parts library](https://github.com/FreeCAD/FreeCAD-library)

## Skill Output:

**Output Type(s):** [JSON data, Parametric CAD model files, CAD export and drawing files, Geometry and validation reports]

**Output Format:** [JSON requests and responses; FreeCAD documents (FCStd) and exports including STEP, IGES, BREP, STL, OBJ, 3MF, DXF, SVG, and PNG]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses report geometry measurements, validation results, and warnings; exported files are read back and checked.]

## Skill Version(s):

2.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
