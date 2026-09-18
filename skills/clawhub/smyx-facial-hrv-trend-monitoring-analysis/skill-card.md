## Description:

Analyzes 30-60 second adult facial videos with remote photoplethysmography to estimate HRV metrics such as SDNN and RMSSD and report trend-oriented stress or fatigue signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Health, wellness, smart mirror, workplace, or care-setting users can use this skill to turn a still adult facial video into contact-free HRV trend indicators. The outputs are intended for personal health trend monitoring and are not a medical diagnosis or a replacement for clinical cardiac evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded face videos and HRV reports are sensitive biometric and health-related data.

Mitigation: Require explicit user consent, document remote processing and retention, and protect stored video and report data with appropriate access controls and encryption.

Risk: Plaintext development endpoints may expose sensitive uploads or reports in transit or route production use to non-production services.

Mitigation: Remove development HTTP defaults before release and require documented production HTTPS endpoints.

Risk: Cloud history access and under-scoped identity handling can expose reports beyond the intended user context.

Mitigation: Require clear user confirmation for cloud history access and use scoped identity checks for report retrieval.

Risk: Local token persistence can leak authentication material from the runtime environment.

Mitigation: Store authentication tokens in a proper secret store and avoid writing reusable credentials to local plaintext files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-facial-hrv-trend-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Smyx analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown report text with optional JSON result output and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include HRV metrics, signal quality, trend direction, stress or fatigue prompts, and historical report links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
