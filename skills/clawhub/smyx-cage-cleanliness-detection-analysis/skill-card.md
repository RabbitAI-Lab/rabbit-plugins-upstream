## Description:

Analyzes pet cage images or videos to estimate feces and urine coverage, score cleanliness, and trigger cleaning alerts for boarding and care facilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to analyze pet boarding, pet shop, animal hospital, or breeding facility cage footage for cleanliness scoring, waste-area estimates, threshold alerts, and historical report review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cage images, videos, report metadata, and stable user or workspace identifiers may be sent to the Life Emergence cloud service.

Mitigation: Use the skill only when this cloud processing is acceptable for the footage and identifiers involved.

Risk: Default development HTTP configuration may expose traffic or credentials if used with real footage or production credentials.

Mitigation: Review and replace the default development networking configuration before production use.

Risk: Automatic account creation and token persistence may create identity and credential-handling concerns.

Mitigation: Review token storage and account initialization behavior before enabling the skill in a shared or production workspace.

Risk: Payment-skill redirection may affect user flow or introduce business-process risk.

Mitigation: Review payment redirection behavior before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Cage Cleanliness API Documentation](artifact/references/api_doc.md)
- [Common Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with JSON-capable analysis reports, report links, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local files or network URLs for image/video analysis, optional pet type, output detail level, and historical report listing.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
