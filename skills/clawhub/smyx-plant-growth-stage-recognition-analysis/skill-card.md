## Description:

Identifies plant growth stages from plant images or videos and returns structured recognition results and report links for precision agriculture decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, agricultural producers, agronomists, and developers use this skill to analyze plant media, classify growth stages, review structured results, and retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, URLs, and identity-linked metadata are sent to the provider's cloud service.

Mitigation: Use the skill only with media approved for upload, obtain first-use consent for uploads and history queries, and avoid submitting sensitive locations or private identifiers.

Risk: The skill silently creates or reuses local user records and stores authentication tokens.

Mitigation: Run it in an isolated workspace, review token and local user storage behavior before deployment, and document retention and cleanup expectations for users.

Risk: Security evidence reports weak disclosure and conflicting transport claims.

Mitigation: Require explicit HTTPS production endpoints, scoped URL validation, and clear disclosure of remote analysis, retention, and token-storage behavior before relying on the release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown text with structured JSON results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save results to a user-specified output file.]

## Skill Version(s):

1.0.12 (source: server release and target metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
