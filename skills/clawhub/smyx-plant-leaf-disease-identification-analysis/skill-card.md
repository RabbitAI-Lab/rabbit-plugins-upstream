## Description:

AI-powered plant leaf disease identification from high-resolution leaf images, detecting lesion features and reporting the most likely disease type with a confidence score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home gardeners, greenhouse operators, and farm inspectors use the skill to analyze plant leaf images or videos, identify likely diseases, and receive confidence scores and general care guidance. It can also retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may still send media to cloud processing, and processing can upload complete files and consume service credits.

Mitigation: Avoid using sensitive media; confirm provider retention and account-deletion terms before processing files.

Risk: Account credentials may be handled unsafely, and local tokens may be retained.

Mitigation: Use only credentials approved for this service and avoid valuable credentials until credential handling is fixed.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured disease analysis report; historical reports can be presented as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes likely disease and confidence score, with general care guidance; it does not provide specific chemical treatment plans.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
