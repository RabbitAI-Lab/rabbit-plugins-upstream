## Description:

Generate a read-only visual dashboard of your ima knowledge base as a self-contained HTML file, with optional tag-based distillation stats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dzz-777](https://clawhub.ai/user/dzz-777)

### License/Terms of Use:

MIT-0

## Use Case:

ima knowledge base users can review a read-only snapshot of their library structure and document counts, with optional tag-based distillation statistics. The skill saves the dashboard as an interactive HTML file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If the bundled chart library is missing, the dashboard can load JavaScript from a remote CDN.

Mitigation: Keep the bundled chart library available, or review and accept the remote CDN fallback before use.

Risk: Inspection of part of the bundled JavaScript was incomplete.

Mitigation: Review the bundled JavaScript and confirm the host runtime enforces the intended file access and write limits.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dzz-777/skills/kb-dashboard)
- [Publisher profile](https://clawhub.ai/user/dzz-777)

## Skill Output:

**Output Type(s):** [Files, HTML]

**Output Format:** [Interactive HTML dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only snapshot with a folder tree, KPI gauges, charts, and a folder-level graph; optional tag-based distillation statistics.]

## Skill Version(s):

1.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
