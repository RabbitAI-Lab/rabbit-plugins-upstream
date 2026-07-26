## Description: <br>
Automates extraction, classification, analysis, and forward planning for work notes from Youdao Cloud Note data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ydyzzjsl](https://clawhub.ai/user/ydyzzjsl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Technical managers, project managers, and similar roles use this skill to turn Youdao Cloud Note work logs into work distribution analysis and future time allocation planning. It helps classify work items, review role focus, identify risks, and generate data-grounded reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for a personal Youdao Cloud Note key and reads private work notes. <br>
Mitigation: Install only if this access is acceptable; use the narrowest folder, title keywords, and time range needed for the analysis. <br>
Risk: Derived analysis findings are saved locally under .workbuddy/memory/. <br>
Mitigation: Delete .workbuddy/memory/ entries after use if retained work summaries are not desired. <br>
Risk: Work notes may contain secrets or sensitive internal information. <br>
Mitigation: Avoid pasting long-lived secrets into ordinary chat or generated reports, and review the HTML reports before sharing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ydyzzjsl/skills/work-summary-plan) <br>
- [Report Generation Specification](artifact/references/report_spec.md) <br>
- [Work Category System](artifact/references/work_categories.md) <br>
- [Work Analysis Report Template](artifact/assets/analysis_report_template.html) <br>
- [Time Allocation Planning Report Template](artifact/assets/planning_report_template.html) <br>
- [Chart.js 4.4.0 CDN](https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance plus generated HTML reports with Chart.js charts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces work item classifications, percentage tables, analysis insights, planning recommendations, two local HTML report files, and derived findings saved under .workbuddy/memory/.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
