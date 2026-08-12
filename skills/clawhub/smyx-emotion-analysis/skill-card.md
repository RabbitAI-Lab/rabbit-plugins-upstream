## Description:

Analyzes face images, videos, or URLs for micro-expression and emotion cues, returning structured reports, recommendations, report links, and history listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to submit face media or media URLs for cloud-based micro-expression analysis and receive structured emotion reports. It also supports querying prior analysis reports linked to the skill's internal user identity handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive face videos/images or URLs through the provider's cloud service.

Mitigation: Use only with appropriate authorization and consent, and avoid submitting sensitive face media unless the provider's cloud processing and retention practices are acceptable.

Risk: Reports are linked to an internal user identity and the security summary notes local token and report-storage concerns.

Mitigation: Review workspace storage, token handling, and report-retention behavior before deployment, especially in shared or regulated environments.

Risk: Micro-expression and emotion outputs can be misleading in high-stakes contexts.

Mitigation: Do not use outputs for truthfulness judgments, psychological diagnosis, employment, legal, or other consequential decisions without qualified human review and independent validation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](artifact/references/api_doc.md)
- [Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud analysis status, emotion scores, key cues, suggestions, historical report tables, and export URLs.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
