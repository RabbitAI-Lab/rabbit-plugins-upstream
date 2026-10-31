## Description:

Analyzes fixed-camera office video to estimate stress indicators by workstation zone and produce group-level heatmaps and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace health teams and managers can use the skill to review aggregated stress trends across office zones and consider changes to work conditions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace footage may contain identifiable employees and is uploaded for remote analysis.

Mitigation: Obtain informed authorization before use and verify the provider's access, retention, and deletion controls.

Risk: Stress analysis can proceed without adequate explicit consent controls.

Mitigation: Require explicit approval before analysis and repair the export-only option before relying on it.

Risk: Credential handling and account storage need stronger controls.

Mitigation: Review and correct credential handling and storage before deployment.

## Reference(s):

- [API interface guide](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis reports and heatmap links; historical reports can be listed in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Group-level, zone-aggregated results; no individual stress assessment]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
