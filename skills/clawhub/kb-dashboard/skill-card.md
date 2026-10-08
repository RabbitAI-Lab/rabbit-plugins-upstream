## Description:

Creates a local HTML snapshot of an ima knowledge base with a folder tree, summary metrics, charts, and a folder-level graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dzz-777](https://clawhub.ai/user/dzz-777)

### License/Terms of Use:

MIT-0

## Use Case:

ima knowledge-base users generate a read-only, single-library or multi-library dashboard to inspect folder structure, document counts, gaps, and folder relationships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated local HTML snapshot contains knowledge-base structure and metadata.

Mitigation: Review and protect the generated file before sharing it, especially for sensitive libraries.

Risk: Charts load ECharts from a CDN and may not render offline or where external scripts are restricted.

Mitigation: Open the dashboard only where CDN access is acceptable; bundle or pin the chart library for sensitive use.

Risk: Dashboard data is inserted into HTML without escaping, which may be unsafe for untrusted knowledge-base text.

Mitigation: Escape dashboard data before rendering and avoid opening snapshots built from untrusted content.

Risk: Broad trigger phrases may activate the skill for unrelated dashboard requests.

Mitigation: Confirm the user wants an ima knowledge-base dashboard before reading their library.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dzz-777/skills/kb-dashboard)
- [ECharts chart dependency](https://cdnjs.cloudflare.com/ajax/libs/echarts/5.5.0/echarts.min.js)

## Skill Output:

**Output Type(s):** [Files, Code]

**Output Format:** [Local HTML dashboard file with embedded knowledge-base snapshot data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only source access; snapshot is not live; charts require access to the ECharts CDN.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
