## Description: <br>
Analyzes fixed-camera doorway or balcony video to detect child exit and return events, estimate daily outdoor activity duration, and produce activity alerts and reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Families, schools, kindergartens, and child-health application developers can use this skill to analyze doorway or balcony camera footage for child outdoor activity sessions, daily duration totals, and parent-facing reminders. It is intended for visual activity statistics and friendly reminders, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sensitive child and home camera footage to cloud services and keeps account-linked report history. <br>
Mitigation: Use only with guardian consent, avoid private or internal URLs, and confirm that cloud processing and report retention match the deployment's privacy requirements. <br>
Risk: The security assessment notes local storage of identity and authentication tokens. <br>
Mitigation: Limit installation to trusted environments and remove local workspace databases and tokens when the skill is no longer used. <br>
Risk: Outdoor time estimates are based on doorway or balcony movement events and may not represent actual exercise or medical status. <br>
Mitigation: Treat outputs as visual activity statistics and reminders, and route health concerns to qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Child outdoor activity monitoring API documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis reports, with optional shell commands for running analysis or listing historical reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include detected events, daily duration totals, alert levels, recommendations, report links, and saved result files when requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
