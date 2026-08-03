## Description: <br>
Detects whether anyone has fallen within a target area, supports video stream analysis, and is suitable for real-time safety monitoring of elderly people living alone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit a local or public video for fall detection, receive a structured analysis report, and review linked historical reports from the cloud service. It is intended for home safety monitoring workflows and should not replace human confirmation or emergency response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may upload sensitive home-monitoring videos to a cloud service for analysis. <br>
Mitigation: Use only with trusted service endpoints, appropriate consent, and video content that is acceptable for cloud processing. <br>
Risk: The skill creates or reuses an internal identity and stores service tokens for later use. <br>
Mitigation: Install only if the publisher and service are trusted; review local token storage, restrict workspace access, and remove persisted credentials when no longer needed. <br>
Risk: Fall-detection results are safety alerts and may be incomplete or incorrect. <br>
Mitigation: Treat reports as prompts for human confirmation and contact family, caregivers, or medical responders when a fall is suspected. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown or JSON text with structured analysis results, risk notes, recommendations, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local video files or public video URLs; historical report listing queries the cloud service for the current identity.] <br>

## Skill Version(s): <br>
1.0.10 (source: ClawHub release evidence; artifact frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
