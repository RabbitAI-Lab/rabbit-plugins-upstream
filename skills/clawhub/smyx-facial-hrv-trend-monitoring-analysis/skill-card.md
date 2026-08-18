## Description:

Analyzes 30-60 seconds of adult facial video with rPPG to estimate HRV metrics such as SDNN and RMSSD and produce trend-oriented health monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and health-operations teams use this skill to submit adult still-face video or video URLs for contact-free HRV trend monitoring, report generation, and history lookup. The outputs are health trend references and are not medical diagnoses or clinical cardiovascular assessments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial video and HRV outputs are sensitive biometric and health-related data sent to the provider backend or linked to report history.

Mitigation: Use only with informed consent, approved data handling, and the minimum necessary video or URL input; treat generated reports as sensitive health trend records.

Risk: Silent identity creation, local token persistence, and history lookup can associate reports with a locally persisted identity.

Mitigation: Avoid shared machines unless the local SQLite database and tokens are protected, removable, or managed under an approved retention process.

Risk: The default configuration may point to non-production or HTTP endpoints.

Mitigation: Review endpoint configuration before use and switch to approved HTTPS production endpoints where required.

Risk: HRV estimates from rPPG can be affected by video quality, movement, lighting, caffeine, emotion, posture, and other conditions.

Mitigation: Use consistent capture conditions, require adequate frame rate and image quality, and present results as trend references rather than medical diagnoses.

## Reference(s):

- [Adult Facial HRV API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown or JSON report text with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HRV metrics, signal quality, trend status, stress or fatigue prompts, recommendations, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
