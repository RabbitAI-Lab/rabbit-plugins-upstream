## Description:

Analyzes workplace camera videos to estimate group-level stress patterns across workstation zones and produce heatmap reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace health and operations teams use the skill to review aggregated stress estimates by workstation zone and consult periodic reports. Its stated purpose is group-level monitoring rather than individual identification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment rates the skill suspicious, citing possible external submission of sensitive video and account or credential handling beyond its stated anonymous workplace-analysis purpose.

Mitigation: Avoid installation unless you can verify that video submission, external processing, account registration, and credential handling are appropriate and authorized.

Risk: The security guidance says the export-only option may still permit analysis, and scanner coverage was partial because a local reference was missing.

Mitigation: Do not rely on the export-only option to prevent analysis; review the complete skill and confirm its behavior before use.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON analysis reports and Markdown history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aggregates results by workstation zone; zones with fewer than three people are reported as insufficient_sample without a stress index.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
