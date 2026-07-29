## Description: <br>
Summarizes local ActivityWatch computer-usage records on macOS, Windows, or Linux, with privacy-preserving fallbacks when records are unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuyewang](https://clawhub.ai/user/liuyewang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and individual users use this skill to summarize local computer activity, app usage, foreground sessions, AFK time, timelines, and project or billable reports from ActivityWatch data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local ActivityWatch records can reveal app usage and window-title context. <br>
Mitigation: Install only when this local activity summarization is acceptable, keep the ActivityWatch API on 127.0.0.1, and avoid uploading or sharing reports without explicit intent. <br>
Risk: CSV or TSV exports can create local files containing sensitive activity metadata. <br>
Mitigation: Save spreadsheet reports only when a local file is intended, and review the destination and contents before sharing. <br>
Risk: Project or billable classification rules may expose client or project patterns. <br>
Mitigation: Review any local rules file before use and keep rules local to the reporting workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liuyewang/skills/computer-usage-summary) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, CSV, TSV, Files, Shell commands, Configuration guidance] <br>
**Output Format:** [Conversational summaries, Markdown tables, JSON, TSV, CSV, and optional local report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Keeps reports local by default; CSV and TSV exports may contain sensitive activity metadata.] <br>

## Skill Version(s): <br>
0.2.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
