## Description:

Estimates concrete volumes and rebar quantity ranges from structural DWG/DXF drawings for floor-level and pour-zone material planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Construction planners and engineers use this skill to prepare preliminary concrete orders and rebar quantity ranges from structural drawings, with floor and pour-zone breakdowns and reports of missing inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted CAD reader dependencies or a configured CAD_SKILL_DIR path could affect local execution.

Mitigation: Install the required cad-file-reader dependency only from a trusted source and verify the configured path before running.

Risk: Drawing-derived caches and quantity reports may expose sensitive project details on disk.

Mitigation: Use --cache-dir to control storage and remove .cadidx and output files when no longer needed.

Risk: Planning estimates and incomplete drawing inputs may lead to incorrect engineering or purchasing decisions.

Mitigation: Review missing-input reports and check quantities against drawings; do not use estimates for fabrication, settlement, or final engineering quantities.

Risk: Bundled noncommercial license terms conflict with the server's MIT-0 license metadata.

Mitigation: Confirm the applicable license and obtain any necessary permission before commercial use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/tujian-suanliang)
- [CAD quantity pipeline guide](packs/quantity-pipeline/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown and CSV reports, JSON records, and optional XLSX spreadsheets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish estimated quantities, missing inputs, concrete grades, and material-planning assumptions.]

## Skill Version(s):

0.9.0 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
