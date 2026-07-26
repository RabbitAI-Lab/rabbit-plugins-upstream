## Description: <br>
Analyzes night-vision bedroom or hallway media to detect elderly bed-exit duration, wandering behavior, and threshold-based alert information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregiving teams, nursing-home operators, and smart-home integrators use this skill to analyze authorized night-bedroom or hallway media for prolonged bed exits and wandering alerts. The skill outputs behavioral statistics and alerts, not medical diagnoses or care instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive night-bedroom video or URLs may be processed by the configured remote service. <br>
Mitigation: Use only authorized media with informed consent from monitored people or guardians, and confirm the remote service is appropriate for the deployment. <br>
Risk: The skill may silently create or reuse an account identity and store access tokens in the workspace. <br>
Mitigation: Run it only in controlled workspaces, restrict access to generated tokens and reports, and rotate or remove stored credentials when access is no longer needed. <br>
Risk: Outputs are behavioral alerts and may be incorrect or incomplete for urgent safety events. <br>
Mitigation: Require caregiver review and immediate human verification for suspected falls, wandering away, or other emergencies. <br>


## Reference(s): <br>
- [API 接口文档](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json] <br>
**Output Format:** [Markdown report text with JSON analysis content and optional report link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save the report text to a caller-specified output file.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
