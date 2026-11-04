## Description:

Classifies plant legends, parses plant-table baselines, and calculates paving area from closed regions in cad-file-reader landscape candidates, producing review-ready budget and material-plan drafts with confidence tiers and evidence coordinates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Landscape estimators and CAD reviewers can turn cad-file-reader landscape candidates into traceable plant-count and paving-area budget drafts. Review flagged candidates and evidence coordinates before using results in a quantity or material plan.

### Deployment Geography for Use:

Global; designed for Chinese construction and landscape drawings, with Simplified Chinese as the default vocabulary and English legend aliases.

## Known Risks and Mitigations:

Risk: The separate CAD reader and optional shared-state components were not included in the security review and may process confidential drawing data.

Mitigation: Use a trusted, reviewed, pinned CAD reader installation and review its shared-state and optional bus components before sharing confidential project data.

Risk: Ambiguous drawing labels, coordinates, layers, units, scale, or boundaries can make quantity candidates incomplete or misleading.

Mitigation: Verify quantities against the source drawings, inspect evidence coordinates and P2/P3 review flags, and treat reports as budget and material-plan drafts rather than final measurements or quotations.

Risk: Generated reports can overwrite files in the selected output folder.

Mitigation: Choose a controlled output folder and check its contents before running the skill.

Risk: The server-reported MIT-0 license conflicts with the packaged CC-BY-NC-SA-4.0 license claims.

Mitigation: Confirm which license governs this release before redistribution or commercial use; the artifact documentation says commercial users should obtain written author authorization.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/yuanlin-suanliang)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)

## Skill Output:

**Output Type(s):** [CSV files, Excel workbook, Markdown report, Review guidance]

**Output Format:** [XLSX, CSV, and Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities include P0–P3 confidence tiers, evidence coordinates, and review flags; they are not final settlement measurements or formal quotations.]

## Skill Version(s):

0.4.34 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
