## Description: <br>
Analyzes fixed-camera emergency shelter media to detect visual acute-stress behaviors such as stupor, tremor, unresponsiveness, and hypervigilance, then produces psychological crisis alerts for human response teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External emergency command teams and licensed psychological rescue staff use this skill to analyze fixed-camera shelter video or images for visual acute-stress behavior alerts, zone/location markers, PFA-oriented response guidance, and report/history lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shelter media and psychological-alert history may be processed through the configured cloud service. <br>
Mitigation: Confirm deployment authorization, retention and deletion rules, and access controls before use. <br>
Risk: The skill may silently create or reuse an identity and persist tokens or local state. <br>
Mitigation: Review whether local credential files and SQLite state are acceptable, protected, and removable in the target environment. <br>
Risk: Behavioral crisis alerts can affect emergency response decisions and may be incorrect or sensitive. <br>
Mitigation: Require human review before escalation, avoid clinical diagnosis, and route interventions through authorized psychological rescue staff. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report text with structured JSON-style fields and optional file output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include crisis level, zone/location markers, temporary tracking IDs, PFA response guidance, report links, and historical alert tables.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter and auto changelog mention 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
