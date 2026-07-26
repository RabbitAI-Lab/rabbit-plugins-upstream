## Description: <br>
Conducts video safety risk analysis for outdoor sports and endurance events, identifying injuries and sudden health risks and producing structured reports with warnings and recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and event operators use this skill to submit outdoor sports videos or URLs for cloud analysis, receive structured risk reports, and query prior reports for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Videos, URLs, and report queries may be sent to the lifeemergence.com cloud service for processing. <br>
Mitigation: Install and use only when that service relationship and media data flow are approved; avoid submitting sensitive media unless policy allows it. <br>
Risk: The skill may silently create or reuse an identity and store service tokens in a local SQLite database. <br>
Mitigation: Run it in an isolated workspace, restrict workspace sharing, and remove local identity or token files when deprovisioning. <br>
Risk: Generated safety reports can influence medical or emergency decisions. <br>
Mitigation: Treat outputs as decision support only and escalate urgent participant health concerns to qualified medical personnel. <br>


## Reference(s): <br>
- [Outdoor sports analysis API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and JSON-formatted structured analysis, with optional result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report links and history-query tables; local video uploads are limited to supported video formats and size limits.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
