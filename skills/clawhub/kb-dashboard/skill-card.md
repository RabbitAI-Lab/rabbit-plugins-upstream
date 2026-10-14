## Description:

Creates a read-only, single-file HTML dashboard showing the structure and summary charts of an ima knowledge base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dzz-777](https://clawhub.ai/user/dzz-777)

### License/Terms of Use:

MIT-0

## Use Case:

ima knowledge-base users can inspect folder structure, document counts, empty areas, and folder-level relationships in a read-only snapshot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Knowledge-base content may cause unsafe scripts to run in the generated dashboard.

Mitigation: Review before installing; use only trusted libraries and collaborators, and avoid shared or externally populated knowledge bases until dashboard data is safely escaped.

Risk: Optional relationship mapping can read full card content, beyond the default structure view.

Mitigation: Enable relationship mapping only on explicit request and only for knowledge bases whose contents you trust.

## Reference(s):

- [kb-dashboard on ClawHub](https://clawhub.ai/dzz-777/skills/kb-dashboard)

## Skill Output:

**Output Type(s):** [Files]

**Output Format:** [Single-file HTML dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Snapshot with folder tree, KPIs, charts, and folder-level graph; charts require an internet connection.]

## Skill Version(s):

1.0.4 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
