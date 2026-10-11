## Description:

Generates preliminary installation-work quantity schedules and material plans from DWG drawings or scan indexes, covering electrical runs, water systems, supports, and equipment without pricing or final settlement quantities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Estimators and MEP engineers use the skill to prepare preliminary quantity takeoffs and material plans from installation drawings, then review exceptions and compare results with specialist estimating tools. It does not provide prices or replace detailed fabrication or settlement measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A CAD measurement import can launch a validator from the locally discovered cad-file-reader dependency.

Mitigation: Install only with a trusted cad-file-reader and CAD_SKILL_DIR path; process only intended local files in a controlled workspace.

Risk: Generated JSON and XLSX files may overwrite existing local outputs.

Mitigation: Review output paths before running and keep backups of files that must be preserved.

Risk: Preliminary quantities may miss vertical runs or include ambiguous and duplicate drawing entries.

Mitigation: Review unmatched and inferred items against drawings and specialist tools before procurement or contractual use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Calculation and standards rules](references/standard_rules.json)
- [Quantity and material mapping rules](references/dual_caliber_rules.json)
- [Allowances and loss rules](references/loss_rules.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance, JSON scan indexes, and multi-sheet XLSX quantity and material-plan drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes matching, confidence, standards-boundary, and manual-review information; measurement candidates are not final quantities.]

## Skill Version(s):

1.0.1 (source: ClawHub release; bundled manifest and frontmatter identify 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
