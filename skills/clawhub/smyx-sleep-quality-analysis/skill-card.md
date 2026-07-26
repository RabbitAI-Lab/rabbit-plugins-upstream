## Description: <br>
Identifies sleep stages including falling asleep, light sleep, deep sleep, and REM; monitors body movement, nighttime awakenings, and sleep apnea for sleep monitoring scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to analyze sleep-monitoring video files or URLs and obtain structured sleep quality reports. It supports sleep stage recognition, body movement statistics, nighttime awakening counts, sleep apnea indicators, report links, and cloud-backed historical report queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive sleep-monitoring videos and report queries are sent to the publisher's cloud service. <br>
Mitigation: Use only media that is appropriate to share with the publisher service, avoid unnecessary personal or clinical content, and review the service destination before deployment. <br>
Risk: The skill can silently create or reuse a persistent local or backend identity and token records. <br>
Mitigation: Review or clear the workspace data directory and stored account records when persistent identity association is not desired. <br>
Risk: Sleep analysis output is health-related and may be incomplete or misleading if treated as a diagnosis. <br>
Mitigation: Present results as sleep-quality reference information and route medical decisions to qualified professionals or validated clinical workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON sleep analysis reports with report links and optional saved text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include structured sleep metrics, sleep-stage summaries, apnea indicators, historical report records, and cloud report export links.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter is 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
