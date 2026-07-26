## Description: <br>
Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing, and butting, and outputs behavior type, intensity level, and alert level. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agricultural operations teams use this skill to screen barn camera media for livestock or poultry conflict events and receive structured behavior, intensity, alert, and report-link outputs. It supports local media files, media URLs, and cloud history lookup for prior analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded livestock media or supplied media URLs are sent to LifeEmergence cloud APIs for processing. <br>
Mitigation: Install and run the skill only where cloud processing of the media is permitted by the user or organization. <br>
Risk: The skill can create or reuse internal identity state and query cloud history associated with that identity. <br>
Mitigation: Review the identity and history-query behavior before deployment, and limit use to environments where local identity persistence is acceptable. <br>
Risk: Service tokens may be stored in a local workspace SQLite database. <br>
Mitigation: Protect the workspace, restrict access to local data files, and remove persisted state when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured analysis text with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include behavior classifications, timestamps or segment lists, locations of involved animals, intensity level, alert level, historical report records, and exported report links.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
