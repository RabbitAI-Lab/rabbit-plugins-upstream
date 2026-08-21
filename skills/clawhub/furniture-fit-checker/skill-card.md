## Description:

Furniture Fit Checker helps an agent check whether furniture can fit through doors, hallways, stairs, elevators, and target room layouts using measurement-based geometry and optional ASCII floorplan previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to evaluate large furniture before purchase or moving day by checking delivery-path clearance, room fit, walkway clearance, and common measurement pitfalls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fit decisions can be wrong if users measure nominal dimensions instead of actual clear openings, narrowest hallway points, stair headroom, or removable furniture parts.

Mitigation: Measure the delivery path at the narrowest points, use clear door openings with doors open, account for ceiling and obstruction clearances, and re-run checks after removing legs or arms when applicable.

Risk: The calculator is intended for rectangular rigid-item geometry and does not model weight, grip, fragile materials, floor protection, or professional moving constraints.

Mitigation: Treat marginal or high-risk moves as conservative signals and use insured professional movers for pianos, glass, mirrors, unusually heavy items, or tight stair and landing turns.

Risk: The release evidence describes a local command-line helper with no hidden data access, persistence, or unsafe authority, but installers still run local code.

Mitigation: Review the local checker script and run it with user-supplied measurements only; no external credentials or network access are required by the evidence.

## Reference(s):

- [Furniture Fit Geometry Reference](references/fit-geometry.md)
- [Furniture Fit Checker README](README.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/furniture-fit-checker)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown with inline shell command examples and text reports from the local checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fit verdicts, clearance warnings, and ASCII floorplan previews when the checker is run.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
