## Description:

Conducts open-ended Q&A on image content based on computer vision and large language models, supporting natural-language answers to user questions about images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask open-ended questions about image content, receive visual analysis responses, and retrieve prior visual Q&A reports when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files and URLs may be sent to the publisher's backend for analysis.

Mitigation: Use only content that is appropriate to share with the publisher's service, and review the configured endpoints before processing private images, videos, or documents.

Risk: The skill may create or reuse persistent identity and token data, and prior reports may be queryable through the skill.

Mitigation: Review token storage and history-report behavior before use in account-sensitive environments, and clear stored credentials or report history according to local policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown text with optional JSON output and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a user-specified file and may include links to cloud-hosted analysis reports.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
