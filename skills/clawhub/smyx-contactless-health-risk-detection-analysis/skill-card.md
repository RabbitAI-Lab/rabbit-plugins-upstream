## Description: <br>
Analyzes frontal face images or videos with multimodal physiological features to provide early health-risk screening and alerts for conditions such as heart attack, stroke, hypertension, and hyperlipidemia. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and care-setting operators use this skill to submit a frontal face image or short video for early health-risk screening and to retrieve prior cloud reports. It supports daily screening workflows for homes, communities, and elderly care facilities, but its results are not a substitute for professional medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive face images, videos, and health-risk report queries are sent to the vendor cloud service. <br>
Mitigation: Use only with informed consent and appropriate privacy approval, and avoid uploading data that is not authorized for vendor processing. <br>
Risk: The skill may silently create or reuse persistent local identities and store tokens in the workspace. <br>
Mitigation: Run it in a controlled workspace, review local credential-storage policy before use, and clear or revoke stored credentials when they are no longer needed. <br>
Risk: Screening output could be mistaken for a medical diagnosis. <br>
Mitigation: Present results as early screening information only and refer high-risk findings to qualified healthcare professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-health-risk-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON report text, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts a local image or video path, a public media URL, history-list mode, detail level, and optional output path; supports jpg/jpeg/png/mp4/avi/mov inputs up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
