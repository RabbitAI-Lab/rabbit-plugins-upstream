## Description:

Analyzes crop leaf, bud, and fruit images or videos through a service API and returns likely pest types with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External growers and agricultural workers can submit crop images or videos to identify likely pests and review estimated counts, affected areas, and confidence scores. The results support early observation and reporting; the skill says it does not provide pesticide or treatment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configuration-only option may still allow media uploads to lifeemergence.com services.

Mitigation: Do not rely on --export-env-only to prevent uploads. Use a corrected release that honors configuration-only mode, and submit only media intended for cloud processing.

Risk: Account creation and token storage safeguards are not clearly explained, and the --api-url option should not be relied on to change the media destination.

Mitigation: Use a dedicated service account, restrict credential destinations, and confirm account and token handling before use.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Structured reports, Markdown]

**Output Format:** [Structured text or JSON reports; Markdown tables for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image and video inputs; each file is limited to 10 MB. Results are for reference and do not include pesticide recommendations.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
