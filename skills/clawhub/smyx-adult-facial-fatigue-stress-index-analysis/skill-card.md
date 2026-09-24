## Description:

Analyzes adult face images or short videos to estimate visual fatigue and stress indicators, return a 0-100 fatigue/stress index, and provide non-diagnostic status guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to analyze clear adult frontal face media for workplace wellness, smart mirror, selfie app, or personal status monitoring workflows. The output is a visual fatigue/stress score and directional advice, not a medical diagnosis or clinical stress assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images and videos may be uploaded to remote analysis services.

Mitigation: Use the skill only with informed consent for biometric processing, and review the configured API endpoints and data handling terms before deployment.

Risk: The skill can create or reuse backend-linked identities and store local tokens for later requests.

Mitigation: Run it in an isolated workspace, restrict access to local data files and SQLite databases, and rotate or delete stored credentials when access is no longer needed.

Risk: History queries can retrieve cloud-linked prior analysis reports.

Mitigation: Limit report access to authorized users and verify that retention, deletion, and access controls match the deployment's privacy requirements.

Risk: Facial fatigue and stress scores can be affected by lighting, makeup, filters, pose, and image quality.

Mitigation: Present results as directional wellness information, avoid clinical claims, and recommend professional review for persistent concerns.

## Reference(s):

- [Adult Facial Fatigue / Stress Index API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text containing structured JSON analysis results, report links, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue/stress score, level, visual feature metrics, contributing features, suggestions, medical follow-up hints, and report export URLs.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
