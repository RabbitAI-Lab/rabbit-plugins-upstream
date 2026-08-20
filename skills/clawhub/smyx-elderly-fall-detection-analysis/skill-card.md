## Description:

Uses vision and radar technology for contactless fall detection in home safety monitoring for elderly people living alone, with seconds-level alarm triggering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, or care-service operators use this skill to submit home-monitoring images, videos, or public media URLs for fall-event analysis and to retrieve structured report history for safety monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home-monitoring images, videos, URLs, identity values, and report history may be sent to the LifeEmergence-backed service.

Mitigation: Use only where cloud analysis is approved, disclose the data flow to affected users, and avoid submitting unrelated private footage or identifiers.

Risk: Automatic identity provisioning, token persistence, and account-linked history retrieval can expose account or report data if the workspace is shared or poorly protected.

Mitigation: Run the skill in an isolated workspace, restrict access to stored credentials and report outputs, and rotate or remove tokens when access is no longer needed.

Risk: Fall-detection output is a safety alert and may be incomplete or incorrect.

Mitigation: Require human confirmation and established emergency-response procedures before acting on alerts.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Smyx analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-fall-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON-formatted analysis/report text with report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a file when --output is provided; analysis can be run from local files or public URLs.]

## Skill Version(s):

1.0.12 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
