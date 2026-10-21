## Description:

Turns landscape CAD scan results into reviewable plant counts, paving-area estimates, and draft materials plans for Chinese landscape projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Landscape estimators and project teams use CAD-derived drawing data to prepare preliminary plant schedules and paving-area estimates with traceable evidence and review flags. Outputs are drafts, not final construction measurements, settlement quantities, or formal quotations.

### Deployment Geography for Use:

China; Chinese-language drawing conventions and regional plant libraries are the default, with project libraries available for other locales.

## Known Risks and Mitigations:

Risk: CAD-derived quantities may be inaccurate where drawing layers, units, or plant references are missing or ambiguous.

Mitigation: Confirm drawing units and scale, and manually review P2/P3 results before using draft quantities for planning.

Risk: Project drawings and optional plant libraries may contain sensitive project information.

Mitigation: Provide only authorized local files and restrict access to generated reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/yuanlin-suanliang)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [CSV reports, an optional XLSX workbook, and a Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plant counts and paving areas include evidence coordinates, confidence levels (P0–P3), and items requiring review.]

## Skill Version(s):

0.4.23 (source: ClawHub release metadata, SKILL.md, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
