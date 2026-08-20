## Description:

This skill analyzes tomato and chili flower or fruit images and videos to count open flowers and young fruits, calculate fruit-set rate, and return a structured report with cultivation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, greenhouse operators, and garden assistants use this skill to evaluate tomato or chili pollination and fruit-set performance from plant media. It supports structured flower and young-fruit counts, fruit-set-rate calculation, report links, and cloud history lookup for prior analyses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, and supplied media URLs may be processed by cloud services and may be included in cloud history retrieval.

Mitigation: Use the skill only with media and URLs approved for cloud processing, and review the service data-handling terms before deployment.

Risk: The skill may silently create or reuse an account identity and store tokens in a workspace SQLite database.

Mitigation: Run it in an isolated workspace, protect the workspace data directory, and clear local identity or token storage when rotating accounts or uninstalling.

Risk: Evidence reports shipped development network/debug settings and mismatched API documentation.

Mitigation: Review configuration endpoints and documentation before normal use, and pin known production endpoints for deployment.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown and structured JSON text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report text to a user-specified output file.]

## Skill Version(s):

1.0.8 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
