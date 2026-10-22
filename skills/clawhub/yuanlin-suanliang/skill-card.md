## Description:

Recalculates landscape CAD recognition candidates into categorized plant counts and paving-area estimates, with confidence tiers and evidence coordinates, for preliminary quantity and materials-planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

External landscape designers, estimators, and project teams can turn landscape CAD recognition results into preliminary plant schedules and paving quantities for budgeting and materials planning. These estimates are drafts and do not replace design review, field verification, completion measurement, settlement, or formal quotations.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional data sharing may execute an unverified local client and give stale or unreviewed project data misleading trust labels.

Mitigation: Use the core quantity calculator without optional statesync until client selection and cache/review handling are corrected. If sharing is enabled, select a trusted installed client and independently verify cached data and review status.

Risk: Preliminary quantities could be mistaken for verified purchasing quantities or quotation figures.

Mitigation: Manually check quantities before purchasing materials or issuing quotations.

## Reference(s):

- [ClawHub release](https://clawhub.ai/lisong2003-lgtm/skills/yuanlin-suanliang)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, JSON, Spreadsheet files]

**Output Format:** [Preliminary quantity and materials-planning reports in Markdown, CSV, JSON, and optional XLSX formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence tiers (P0–P3), evidence coordinates, and items requiring review; estimates are not authoritative measurements or quotations.]

## Skill Version(s):

0.4.25 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
