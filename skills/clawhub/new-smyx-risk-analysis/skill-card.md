## Description: <br>
Supports identifying high-risk behaviors and health risks through video/images, including elderly falls, precursors to heart attacks and strokes, and abnormal behaviors, issuing timely warning alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, safety teams, and developers use this skill to analyze video or image inputs for falls, abnormal behavior, and visual health-risk indicators, then receive structured risk results, recommendations, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded videos/images and derived health-risk results are sent to LifeEmergence remote services. <br>
Mitigation: Use only approved media, confirm consent from affected people, and review the service's data handling and retention expectations before installation. <br>
Risk: The skill stores identity/account metadata and tokens in a local SQLite database. <br>
Mitigation: Run it in a controlled workspace, restrict access to workspace data, and clear or rotate stored credentials when the skill is no longer needed. <br>
Risk: Health and safety detections may be incomplete or incorrect and should not replace professional medical, emergency, or security judgment. <br>
Mitigation: Treat outputs as decision support, require human review for alerts, and escalate urgent events through appropriate professional channels. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-risk-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Risk category reference](artifact/references/risk_categories.md) <br>
- [API interface reference](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown-formatted text with structured JSON content, risk recommendations, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analysis results may include derived health-risk and behavior-risk findings, history report records, and report export URLs returned by remote services.] <br>

## Skill Version(s): <br>
999.999.1001 (source: ClawHub release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
