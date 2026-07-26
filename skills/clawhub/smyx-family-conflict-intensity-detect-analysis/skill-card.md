## Description: <br>
Using a fixed camera with microphone in the living room, the skill analyzes audio and video to estimate sound intensity, body-movement intensity, and a low, medium, or high family conflict intensity level. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and family-support professionals use this skill to process consented household audio/video or video URLs and produce conflict-intensity indicators, gentle reminders, and report links. It is intended as an auxiliary monitoring and reporting tool, not a legal, psychological, or emergency-response service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Household audio/video or video URLs may be sent to external LifeEmergence services for processing. <br>
Mitigation: Use only with explicit informed consent from affected household members and only where cloud processing is acceptable; prefer minimized, masked, or metric-only workflows when available. <br>
Risk: The skill may create or reuse account identity, persist token data, and retrieve account-linked historical conflict reports. <br>
Mitigation: Review local identity and token storage before installation, restrict access to report history, and remove stored credentials or identifiers when the deployment no longer needs them. <br>
Risk: Conflict intensity estimates can be wrong or misleading in sensitive household situations. <br>
Mitigation: Treat outputs as advisory indicators; do not label people as perpetrators or victims, do not use the skill as a substitute for legal or mental-health support, and do not trigger emergency actions without prior consent and human review. <br>


## Reference(s): <br>
- [Family Conflict Intensity API Documentation](artifact/references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-intensity-detect-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured report text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include acoustic metrics, visual metrics, conflict intensity level, alert type, gentle reminder text, recommended action, and report export URLs.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
