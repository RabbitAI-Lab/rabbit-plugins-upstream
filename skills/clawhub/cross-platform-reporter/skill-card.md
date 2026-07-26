## Description: <br>
A cross-platform operations reporting skill that automatically collects metrics from Xialiao, AIWay, MEYO, Tieba, and DingTalk, then generates structured weekly reports and trend analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bdz2007-antgroup](https://clawhub.ai/user/bdz2007-antgroup) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations teams, community managers, and analysts use this skill to collect account and engagement metrics across five platforms and prepare weekly performance reports with highlights, trend analysis, and next-week strategy notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to collect data from five platforms and store local account state, which may expose sensitive account or engagement data. <br>
Mitigation: Use only accounts you control, confirm each platform API's read scope before use, and inspect accounts-state.json for sensitive data before sharing or retaining it. <br>
Risk: The skill describes automatic publishing of weekly reports to MEYO, which could disclose inaccurate, private, or unreviewed operational information. <br>
Mitigation: Require manual review and approval before any generated report is published to MEYO or another external channel. <br>


## Reference(s): <br>
- [Cross Platform Reporter on ClawHub](https://clawhub.ai/bdz2007-antgroup/skills/cross-platform-reporter) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Configuration, Guidance] <br>
**Output Format:** [Markdown report template with structured tables, bullet summaries, and workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local account state in accounts-state.json and platform account metrics collected during the reporting workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
