## Description: <br>
Identifies strangers in surveillance images or video by comparing faces against a known-person database and returning structured recognition results, alerts, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security teams, property managers, and access-control operators use this skill to analyze surveillance images, video, or report history for stranger recognition and warning workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Surveillance images or video URLs may be sent to the configured cloud service for biometric analysis. <br>
Mitigation: Use only approved media and endpoints, and confirm consent, access controls, and data-retention expectations before use with real footage. <br>
Risk: The skill manages persistent local and remote identity state and stored tokens around sensitive reports. <br>
Mitigation: Review account and token storage behavior, isolate deployments by user or workspace, rotate credentials, and remove stale identity state when access changes. <br>
Risk: Face enrollment can change the known-person database used for future stranger-recognition decisions. <br>
Mitigation: Restrict enrollment permissions, verify person identity before enrollment, and review thresholds and report results before operational action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface notes](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Markdown or JSON reports, with optional local file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include recognition summaries, warning text, history tables, enrollment responses, and report links.] <br>

## Skill Version(s): <br>
1.0.8 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
