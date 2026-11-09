## Description:

Split an A-share shareholder-return filing into eight verbatim cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External users reviewing A-share dividend, buyback, reduction, or pledge announcements use this skill to record each filing statement with a source anchor and identify missing information, while leaving investment judgments to a person.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security evidence marks the skill suspicious because scanners report an external catalog lookup and sending user-provided document references to an external service without a privacy warning; the scan is partial.

Mitigation: Review the external request and privacy handling before sending document references; use the user-supplied text or local-file path when references should not be sent externally.

Risk: The security scan is incomplete because a referenced local path could not be resolved.

Mitigation: Resolve the missing path and review the remaining component before installation; do not treat the partial scan as a complete assessment.

## Reference(s):

- [Shareholder return terms and eight-item checklist](references/sh-return-terms.md)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Five-section Markdown note with eight quoted announcement items and source anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes missing-item accounting and a human-review section; does not provide investment judgments.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata, SKILL.md frontmatter, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
