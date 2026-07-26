## Description: <br>
Turn user-provided numbers into a bar, line, area, pie, or doughnut chart spec with a one-line reading of the result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and other users use this skill to convert supplied numeric tables, lists, or metrics into a renderable chart JSON block and a concise takeaway. It is suited for trend, comparison, and composition visualizations where the user provides the data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated chart JSON or the one-line insight may misrepresent the supplied data if the chart type, labels, series lengths, units, or scale are wrong. <br>
Mitigation: Review the chart type, labels, series lengths, units, numeric values, and takeaway before using or publishing the chart. <br>
Risk: Sensitive business data may be exposed if confidential metrics are pasted into the chat context. <br>
Mitigation: Use approved data only, redact confidential values when possible, and review generated JSON before sharing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/chart) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/chart.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown with a one-line insight and a fenced chart JSON block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The chart spec must be valid JSON with matching labels and numeric series data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
