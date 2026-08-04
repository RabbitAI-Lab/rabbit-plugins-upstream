## Description: <br>
Evaluates plant images, optional environmental data, and growth metrics to produce a 0-100 plant vitality score with a trend and structured report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, and plant-monitoring developers use this skill to analyze plant images or videos, calculate vitality scores and trends, and retrieve historical plant vitality reports for smart planters, plant factories, home gardening, and monitoring platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, URLs, identity values, and analysis metadata may be sent to the LifeEmergence remote service. <br>
Mitigation: Use the skill only when the remote service account, retention model, and media sensitivity are acceptable; avoid submitting sensitive media. <br>
Risk: The skill silently creates or reuses an account identity and stores login tokens locally. <br>
Mitigation: Run it in an isolated workspace when possible, review or clear the workspace data directory after use, and avoid sharing the local token database. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Plant Vitality API Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown result text with optional JSON detail, report links, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write analysis output to a user-specified file; historical report queries are formatted as Markdown tables.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
