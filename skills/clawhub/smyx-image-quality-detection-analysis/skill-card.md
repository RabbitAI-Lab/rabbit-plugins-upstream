## Description: <br>
Detects camera image and video quality issues such as black or white screens, color cast, stripes, noise, and blurriness for surveillance self-check and maintenance workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security, operations, and camera maintenance users can submit local or URL-based images and videos to check for common camera-feed quality problems. The skill can also retrieve cloud-hosted historical quality analysis reports associated with the local identity used by the workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Camera images, videos, and report metadata may be sent to external lifeemergence.com and open.lifeemergence.com cloud services. <br>
Mitigation: Use only with media approved for that service, and review the service's privacy, retention, and access-control terms before processing confidential surveillance footage. <br>
Risk: The skill can create or reuse a local identity and cache tokens in the workspace data directory. <br>
Mitigation: Run it in a trusted workspace with appropriate filesystem access controls, and clear local identity or token data when the workspace is shared or retired. <br>
Risk: Image quality analysis is intended for maintenance support and may not identify every equipment or environmental failure. <br>
Mitigation: Treat results as decision support and confirm critical findings with operational checks or professional hardware inspection. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Markdown and JSON-like structured analysis text, with optional saved text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include analysis status, structured quality findings, historical report tables, and report export links.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub release evidence; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
