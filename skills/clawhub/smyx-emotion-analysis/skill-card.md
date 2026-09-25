## Description:

Analyzes submitted face videos or video URLs for micro-expressions and returns structured emotion reports, recommendations, history results, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit face video files or URLs for remote micro-expression emotion analysis and to retrieve identity-linked historical reports. It is suited for structured report generation and exploratory behavior analysis, not for sensitive decisions or private biometric media without additional review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive face videos and identity-linked reports through a remote emotion-analysis service.

Mitigation: Use only with appropriate consent and non-sensitive media; confirm publisher retention, access controls, and identity-linkage behavior before deployment.

Risk: Evidence security guidance identifies unsafe default networking and local reusable credential storage.

Mitigation: Review before installing, require HTTPS production endpoints, remove development HTTP defaults, and protect or clear local identity and token storage.

Risk: Emotion and micro-expression analysis can be unreliable for high-impact judgments.

Mitigation: Treat results as informational guidance only and keep human review in place for any consequential assessment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis, report summaries, history listings, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally write result JSON to a user-specified output file; accepts local mp4/avi/mov videos up to 10 MB or video URLs.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
