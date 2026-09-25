## Description:

AI-powered fruit ripeness grading for tomatoes and strawberries that analyzes images or video for fruit color, colored-area ratio, gloss, and relative size, then returns maturity grades and harvest guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, greenhouse operators, home gardeners, and agricultural cooperatives use this skill to grade tomato or strawberry ripeness from fruit images or videos. It helps identify harvest timing by returning structured maturity classifications, visual analysis results, recommendations, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports cloud identity use, local token storage, history lookup, and plaintext development HTTP endpoints.

Mitigation: Review carefully before installing and avoid private media or account-sensitive workflows unless the publisher provides production HTTPS-only configuration, documents cloud uploads and report-history behavior, and provides controls to delete stored local tokens and identity data.

Risk: Ripeness analysis is decision support and may not satisfy commercial grading standards on its own.

Mitigation: Use results as harvest guidance and verify commodity-grade decisions against applicable enterprise or market standards.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fruit-ripeness-grading-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports, with optional report-link tables for historical results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file input, URL input, optional output file writing, and history-list retrieval through cloud API calls.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
