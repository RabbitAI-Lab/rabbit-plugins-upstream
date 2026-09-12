## Description:

Identifies prone sleeping positions, head covering, and occlusion of the mouth or nose by bedding or clothing, then returns high-risk infant sleep safety alerts and structured analysis results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers and developers use this skill to analyze infant sleep-monitoring videos or video URLs for prone sleeping, head covering, and mouth or nose occlusion risks. The skill supports current analysis and cloud history lookup, but its alerts are only an aid and do not replace adult supervision or medical judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send infant sleep videos, video URLs, internal user identifiers, and authentication tokens to a remote service.

Mitigation: Use it only with clear consent and an approved service configuration; avoid real child-monitoring media until retention, access, and privacy terms are confirmed.

Risk: The package includes development and test configuration that uses plaintext HTTP endpoints.

Mitigation: Review configuration before installation and require HTTPS production endpoints for any real media or identity data.

Risk: Reusable account data and tokens may be stored locally for repeated report access.

Mitigation: Run the skill in an isolated workspace, restrict filesystem access, remove stored credentials after use, and rotate exposed tokens.

Risk: Infant asphyxia warnings can be missed, delayed, or inaccurate and are not a substitute for supervision.

Mitigation: Treat every alert as decision support only; caregivers should immediately check the infant and seek medical help when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis content, report links, and optional saved result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include risk factors, safety suggestions, current analysis results, and cloud history records.]

## Skill Version(s):

1.0.14 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
