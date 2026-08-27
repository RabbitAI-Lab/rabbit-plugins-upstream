## Description:

Detects visual signs of white-spot, hyperemia, and fin-rot symptoms from aquarium or underwater fish images and videos, then returns symptom classifications, confidence, location, severity, suggested non-medication actions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarium keepers, public aquarium teams, ornamental fish farm operators, and integration developers use this skill to analyze high-resolution fish images or videos for visible surface-symptom signals and to review structured health reports or history links. The skill is for visual symptom classification and triage support, not final diagnosis or treatment planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium images, videos, or URLs are sent to a remote service for analysis.

Mitigation: Disclose remote processing before use, confirm that users are authorized to submit the media, and avoid submitting sensitive or unnecessary footage.

Risk: History lookup and report access may be associated with an automatically resolved internal identity.

Mitigation: Require explicit user confirmation before history lookup and clearly explain account association and report-retention behavior.

Risk: Reusable account tokens may be persisted in a local workspace database.

Mitigation: Restrict local workspace access, review token storage before shared deployments, and rotate or remove tokens when the workspace changes hands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis)
- [API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with JSON-formatted analysis details, confidence values, severity labels, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report text to a user-specified output file.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
