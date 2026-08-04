## Description: <br>
Analyzes face images, videos, or video URLs for micro-expression and emotion signals, then returns structured reports and report-history lookups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit face media or video URLs to a configured cloud service for micro-expression and emotion analysis, and to retrieve prior analysis reports. Its outputs should be treated as advisory and should not be used for employment, school, law enforcement, health, deception, or other consequential decisions without explicit consent and independent review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive face images, videos, video URLs, and report-history requests are sent to a configured cloud service. <br>
Mitigation: Use only with informed consent, approved data handling, and media that is appropriate to send to the configured service. <br>
Risk: The skill can create or reuse an internal account identity and store tokens or profile data locally under the workspace data directory. <br>
Mitigation: Restrict workspace access, review local token/profile storage before deployment, and clear stored identities when they are no longer needed. <br>
Risk: Emotion, truth, or deception-style outputs may be misleading if used as determinations about people. <br>
Mitigation: Treat results as advisory signals only and avoid consequential use cases without explicit consent and independent expert review. <br>
Risk: Analysis quality can vary with video quality, lighting, face angle, occlusion, file type, and file size. <br>
Mitigation: Use clear, frontal, unobstructed media within the documented format and size limits, and review outputs before relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands] <br>
**Output Format:** [Markdown reports or JSON, with optional saved output files and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local media paths, video URLs, analysis type selection, detail level selection, and cloud report-history listing.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
