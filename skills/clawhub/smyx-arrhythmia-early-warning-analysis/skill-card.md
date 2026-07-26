## Description: <br>
Based on facial video, identifies abnormal rhythms such as premature beats, atrial fibrillation, tachycardia/bradycardia, assists in early detection of heart health risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and health-analysis agents use this skill to screen uploaded facial video for early warning signs of arrhythmia risk and to retrieve prior cloud-hosted analysis reports. Results are screening outputs only and should not replace ECG testing or diagnosis by a cardiology professional. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Facial video and health-analysis results are processed by a remote LifeEmergence service and may be linked to a persistent local identity. <br>
Mitigation: Use the skill only with appropriate consent and data-handling approval, and avoid uploading sensitive health media unless remote processing is acceptable. <br>
Risk: The skill can create or reuse a local identity and store authentication tokens in the workspace data directory. <br>
Mitigation: Review or clear the workspace data directory before and after use when persistent identity or token storage is not desired. <br>
Risk: Arrhythmia findings are screening outputs and may be incorrect or incomplete. <br>
Mitigation: Treat results as early warning information only and require professional ECG testing or cardiology review for medical decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Structured report text with JSON details, Markdown tables for history lists, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the returned report text or JSON to a caller-specified output file.] <br>

## Skill Version(s): <br>
1.0.11 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
