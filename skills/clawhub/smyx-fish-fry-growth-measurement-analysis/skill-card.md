## Description: <br>
Measures fish fry body length from images or videos that include a known-size reference object, then reports growth rate, population statistics, growth curves, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquaculture operators, ornamental fish breeders, lab teams, and developers use this skill to analyze reference-calibrated fry tank media, measure body length in millimeters, track growth rate over time, and review cloud-backed historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send images, videos, URLs, and account-linked context to remote services. <br>
Mitigation: Review the remote-service workflow before installing, use only approved media, and deploy only where users accept the cloud analysis and history-query behavior. <br>
Risk: The skill can silently create or reuse an internal identity and persist user or token data locally. <br>
Mitigation: Manage the workspace as sensitive, limit access to generated local data and credentials, and clear stored identity material according to the operator's retention policy. <br>
Risk: Fish length and growth-rate results can be misleading if the reference object is missing, not on the same plane as the fry, or captured from a non-vertical angle. <br>
Mitigation: Require a known-size reference object, strict top-down capture, confidence checks, and an unreliable-measurement result when calibration or posture conditions are not met. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like text reports from a command-line wrapper] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured measurements, growth statistics, recommended actions, report links, and cloud history tables when the remote service returns them.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
