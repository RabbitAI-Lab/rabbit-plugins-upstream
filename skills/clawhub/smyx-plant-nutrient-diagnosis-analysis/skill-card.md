## Description:

AI-powered plant nutrient deficiency diagnosis from leaf images that analyzes color and morphology changes, compares them with common nutrient-deficiency symptoms, and returns likely deficient nutrients with confidence and guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, home gardeners, greenhouse operators, and agents use this skill to diagnose likely plant nutrient deficiencies from leaf images or videos and to retrieve prior cloud analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded plant media, supplied media URLs, and report-history requests are sent to the publisher's backend services.

Mitigation: Use only media that is appropriate for third-party processing, review configured endpoints before deployment, and avoid submitting sensitive images or URLs.

Risk: The skill can silently create or reuse a local identity and persist account tokens or report history in workspace data.

Mitigation: Clear local smyx data and tokens when persistent account association is not desired, and run the skill in a workspace with appropriate data-retention controls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [Plant Nutrient Diagnosis API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Usage Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned report text to a user-specified output file.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
