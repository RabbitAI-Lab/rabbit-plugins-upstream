## Description: <br>
AI-powered pest and disease detection for rose images or videos that identifies common issues such as black spot, powdery mildew, spider mites, and aphids, estimates severity, and returns general care suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External gardeners, rose growers, and operators of garden or production monitoring workflows use this skill to analyze rose leaf, shoot, bud, image, or video inputs for visible pest and disease symptoms and receive severity grading with general care guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rose images, videos, and submitted URLs may be sent to the publisher's cloud service for analysis. <br>
Mitigation: Use only media the user is comfortable sharing with the publisher's service, and review the publisher's endpoint, retention, deletion, and consent practices before deployment. <br>
Risk: The skill may silently create or reuse a local identity and store token-like data in the workspace data directory. <br>
Mitigation: Review account creation, local identity handling, and token storage behavior before installation, and restrict workspace access where this skill runs. <br>
Risk: History retrieval depends on cloud-stored reports associated with the local or resolved identity. <br>
Mitigation: Confirm that users understand cloud report history behavior and have a deletion or retention process appropriate for the deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-rose-pest-disease-detection-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with detected issue type, severity, suggestions, and report links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image/video files or URLs; history listing output is presented as a Markdown table.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
