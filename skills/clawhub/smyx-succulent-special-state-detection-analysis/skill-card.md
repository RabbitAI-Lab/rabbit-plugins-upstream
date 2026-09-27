## Description:

AI-powered succulent image and video analysis that detects black rot, leaf melting, and stretching, then returns anomaly type, severity, confidence, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, plant-care operators, greenhouse staff, and developers use this skill to analyze succulent images or videos for special health states and review structured results or historical cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or URLs submitted for analysis are processed by lifeemergence.com services.

Mitigation: Use only media and URLs that are appropriate for third-party cloud processing, and avoid confidential plant-location or operational imagery unless the service has been approved for that data.

Risk: Cloud report history is tied to an internal identity and local workspace data can store account tokens.

Mitigation: Review the local identity and token handling before use, isolate the workspace for sensitive environments, and remove or rotate stored credentials when access should end.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with JSON-style structured analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a file and can list cloud report history for the resolved internal identity.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
