## Description: <br>
Alibaba Quark Scan helps agents enhance document and image scans through an external scanning service, including clarity improvement, shadow removal, watermark removal, crop correction, and related single-image processing modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, independent builders, enterprise teams, and automation workflows can use this skill to route a single document or image input to one of the supported scan-enhancement modes and return the processing result. It is intended for static image enhancement, not video, live camera streams, or batch processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User images may be sent to an external scanning service for processing. <br>
Mitigation: Only submit documents the user is comfortable sending to that service, and confirm data-handling expectations before processing sensitive content. <br>
Risk: The skill asks agents to run an unspecified script with image inputs and an API key. <br>
Mitigation: Verify the actual script implementation and command arguments before allowing exec commands, and keep SCAN_WEBSERVICE_KEY scoped and rotated. <br>
Risk: The artifact includes unrelated vulnerability scanning, compliance, risk scoring, and threat-intelligence claims. <br>
Mitigation: Use the skill only for the documented image-enhancement workflow unless separate implementation evidence supports those security-product capabilities. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/alibaba-quark-scan) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful processing may return a local image path; each call handles one static image and the artifact documents a 5 MB local-file limit.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
