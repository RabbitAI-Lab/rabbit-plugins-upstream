## Description:

Generates decoration budget estimates and material plans from room data and construction documents, with CAD measurement candidates retained as inputs for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Construction estimators and site or technical staff use this skill to prepare preliminary interior-decoration quantity estimates and material plans from room schedules, drawings, and project-specific practices. The results are drafts for review and are not intended for settlement, final measurement, or formal quotations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency setup may still run when the offline setting is enabled.

Mitigation: Review dependency setup before installation; do not rely on the offline setting alone.

Risk: Optional data synchronization may execute automatically selected development scripts.

Mitigation: Use a trusted, explicitly selected synchronization client or avoid optional synchronization commands.

Risk: Shared project data remains on disk and may be stale or from an untrusted source.

Mitigation: Check its source and freshness before reusing shared project data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)

## Skill Output:

**Output Type(s):** [Files, Markdown, Configuration]

**Output Format:** [Excel workbook and CSV files, with a Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-dependent estimates with calculation formulas, source references, missing-item checks, and review flags.]

## Skill Version(s):

0.9.27 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
