## Description:

Identifies prone sleeping positions, head covering, and mouth or nose occlusion by bedding or clothing, then returns high-risk infant sleep safety alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers use this skill to analyze infant sleep monitoring videos or video URLs for prone sleeping, head covering, and mouth or nose occlusion risks. The skill can also return identity-linked cloud history for prior warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant sleep videos or video URLs may be sent to a backend for processing.

Mitigation: Install only when the publisher and backend are trusted, and confirm that users understand where footage is processed and retained.

Risk: The skill can create or reuse an internal identity, store account tokens locally, and retrieve cloud report history tied to that identity.

Mitigation: Run in an isolated workspace, review local token storage before use, and avoid shared workspaces for sensitive child footage or reports.

Risk: Automated alerts and reports may be treated as a substitute for direct adult supervision or professional care.

Mitigation: Present the output as auxiliary monitoring only and require caregivers to verify high-risk alerts directly and seek appropriate medical help when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files]

**Output Format:** [Markdown reports and JSON strings, with optional saved text or JSON output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local mp4, avi, or mov video files up to 10 MB, or public video URLs; can list cloud report history associated with the resolved identity.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
