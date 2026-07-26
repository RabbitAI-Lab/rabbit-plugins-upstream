## Description: <br>
Identifies common abnormal pet behaviors in uploaded or linked pet video, including scratching, biting, destructive chewing, jumping, digging, chasing, and separation anxiety, and returns structured behavior reports and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners, trainers, and agents assisting them use this skill to submit pet monitoring videos or URLs for behavior recognition and to retrieve cloud-hosted report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos or video URLs are sent to lifeemergence.com cloud services for processing. <br>
Mitigation: Install and use the skill only where that cloud processing model is acceptable for the video content and workspace. <br>
Risk: The skill may silently create or reuse an external account identity and store authentication state in a local SQLite database. <br>
Mitigation: Review the identity linkage and local state behavior before deployment, and use it only where persistent service tokens and report association are acceptable. <br>
Risk: The scanner verdict is suspicious because the cloud analysis purpose is coherent but account and token handling provide limited user control. <br>
Mitigation: Review the skill before installing and restrict it to environments where the external account linkage and cloud report history model have been approved. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-behavior-detection-analysis) <br>
- [Pet Behavior Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown or JSON report text with optional saved output file and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts a pet video file path or video URL, and can list cloud report history linked to the workspace identity.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence; artifact frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
