## Description:

Helps construction teams estimate concrete quantities and reinforcement ranges from DWG/DXF structural drawings for floor-by-floor material planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Construction planners and engineers use the skill to prepare floor- and pour-zone material plans from structural CAD drawings, including concrete order quantities, strength grades, and approximate reinforcement ranges. Its estimates need drawing review and are not suitable for final takeoff, rebar detailing, or settlement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may download the cad-file-reader dependency into the local skills directory.

Mitigation: Review the dependency and installation behavior before enabling setup.

Risk: Generated caches and reports may contain project drawing information.

Mitigation: Review and protect generated files according to the project's data-handling requirements.

Risk: Quantity and reinforcement estimates may be mistaken for final measurements.

Mitigation: Verify against the drawings and use results for planning, not final takeoff, settlement, or rebar detailing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/tujian-suanliang)
- [Quantity pipeline guide](packs/quantity-pipeline/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown reports and CSV tables, with optional XLSX spreadsheets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes estimated concrete quantities, reinforcement ranges, and review flags; may create local drawing-derived caches.]

## Skill Version(s):

0.9.20 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
