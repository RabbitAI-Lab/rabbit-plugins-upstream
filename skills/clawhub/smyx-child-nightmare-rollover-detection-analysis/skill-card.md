## Description: <br>
Analyzes child nighttime audio/video to report rollover frequency, crying, sleep talk, sleep quality, and possible restless-sleep or nightmare alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, caregivers, and developers integrating child sleep monitoring workflows can use this skill to analyze consented nighttime audio/video and produce behavior statistics, alerts, and report links. It is an assistive monitoring tool, not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Children's bedroom audio/video may be sent to or fetched by a third-party cloud service. <br>
Mitigation: Use only recordings with guardian consent after verifying endpoint trust, retention and deletion terms, and data handling controls. <br>
Risk: Results may be linked to a persistent identity and local tokens. <br>
Mitigation: Review local token storage and account-linking behavior before deployment, and rotate or delete stored credentials when no longer needed. <br>
Risk: Sleep-quality and nightmare alerts could be mistaken for a medical diagnosis. <br>
Mitigation: Present results as assistive behavior statistics and advise professional pediatric or sleep-medicine consultation for persistent concerns. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with optional JSON details, report links, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a caller-specified file; historical report listings are presented as Markdown tables.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter states 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
