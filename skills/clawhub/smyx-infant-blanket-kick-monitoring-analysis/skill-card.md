## Description: <br>
Identifies infants kicking off blankets or exposing their bodies during sleep and returns monitoring results, suggestions, and report links for caregiver review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers and operators use this skill to analyze infant sleep monitoring media for blanket-kicking or body-exposure events and to review current or historical cloud reports. Results are auxiliary reminders and do not replace direct child supervision or safe sleep practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Nursery media or media URLs may be uploaded to the publisher's cloud service for analysis. <br>
Mitigation: Use only with explicit caregiver consent, avoid unnecessary sensitive footage, and confirm the publisher's retention, deletion, and access-control practices before deployment. <br>
Risk: Reports may be linked to a persistent local or backend identity and retained for report history. <br>
Mitigation: Review account/token storage behavior, report-link access controls, and deletion procedures before using the skill with child-monitoring footage. <br>
Risk: Monitoring output may be mistaken for a substitute for direct infant supervision. <br>
Mitigation: Present results as auxiliary reminders only and keep human supervision and safe sleep practices as the primary safety control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-monitoring-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report text, with optional saved output file and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local media paths, media URLs, report-list queries, optional API endpoint configuration, and basic/standard/json detail levels.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
