## Description: <br>
Analyzes adult frontal face images or short videos to estimate visual fatigue and stress indicators, produce a 0-100 fatigue/stress score, and return structured results with directional wellness suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to evaluate adult facial fatigue/stress signals from submitted images, videos, or URLs and to retrieve prior cloud reports. The output is for personal status monitoring and workplace wellness support, not medical diagnosis or clinical stress assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive face images, videos, or URLs are sent to external services for cloud processing. <br>
Mitigation: Use only with informed subject consent and with media appropriate for external cloud analysis. <br>
Risk: The skill may create or reuse an internal identity and retrieve prior cloud reports with limited user control. <br>
Mitigation: Review identity and report-history behavior before installation, especially in shared or enterprise environments. <br>
Risk: Local credential persistence may occur as part of API access. <br>
Mitigation: Install only where local token storage is acceptable and manage the runtime environment as sensitive. <br>
Risk: Single-image fatigue or stress scoring can be affected by lighting, makeup, filters, pose, and image quality. <br>
Mitigation: Treat results as directional wellness guidance and not as medical diagnosis or clinical stress assessment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-adult-facial-fatigue-stress-index-analysis) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown or JSON structured report with report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include face-detection status, fatigue/stress score, level, contributing facial features, suggestions, medical follow-up hint, and history report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
