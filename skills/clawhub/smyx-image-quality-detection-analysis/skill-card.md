## Description:

Detects quality issues in camera footage such as black/white screens, color cast, stripes, noise, and blurriness for security surveillance and camera self-check scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to inspect camera images, video frames, or media URLs for quality problems such as black screens, overexposure, color cast, stripe interference, noise, blur, and clarity issues. It can also retrieve cloud-hosted historical image-quality analysis reports associated with the internal account identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera images, videos, or media URLs may be sent to lifeemergence/open.lifeemergence services for analysis.

Mitigation: Use non-sensitive media unless the external service, retention policy, and account-linking behavior are approved for the deployment environment.

Risk: The skill can create or reuse an internal identity, query cloud report history, and store account tokens in a local SQLite database.

Mitigation: Run it in a scoped workspace, protect local database files, and clear stored credentials when the skill is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [CLI/API output as Markdown report text, Markdown tables for report lists, or JSON text depending on detail mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional output-file writing and cloud report links; analysis is intended as maintenance guidance, not a substitute for hardware inspection.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
