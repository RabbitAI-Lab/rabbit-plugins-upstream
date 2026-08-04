## Description: <br>
This skill analyzes living-room camera audio/video or video URLs to estimate family or couple conflict intensity and return structured acoustic, visual, alert, recommendation, and report-link outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, family counselors, mediation staff, and smart-home application developers can use this skill to analyze consented household conflict media and produce conflict-intensity indicators, gentle reminders, and historical report listings. It is not a substitute for legal, psychological, emergency, or personal-safety services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Household conflict audio/video is highly sensitive and may be sent to configured Life Emergence services. <br>
Mitigation: Use only with explicit consent from all recorded adults, confirm service retention and deletion terms before deployment, and prefer anonymized or masked capture modes where available. <br>
Risk: Reports may be tied to an automatically managed persistent identity and local account tokens. <br>
Mitigation: Run the skill in a controlled workspace, restrict access to the workspace data directory, and delete or rotate local identity and token files when the skill is no longer needed. <br>
Risk: The security evidence flags insufficient user control and contradictory privacy claims. <br>
Mitigation: Review the configured endpoints, report access controls, retention behavior, and emergency-contact behavior before any production use. <br>
Risk: Conflict-intensity outputs can be misused as determinations of abuse, legal status, mental health condition, or personal safety. <br>
Mitigation: Treat outputs as limited acoustic and visual indicators, avoid labeling any party, and route urgent safety concerns to qualified local support or emergency services outside the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-intensity-detect-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured text with conflict metrics, reminders, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can optionally save the returned report text to a user-specified output file and can list historical reports from the configured cloud service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
