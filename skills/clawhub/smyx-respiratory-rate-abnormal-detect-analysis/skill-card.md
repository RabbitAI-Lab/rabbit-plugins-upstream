## Description:

Analyzes video of a resting pet to estimate its breathing rate, compare it with species and body-size reference ranges, and flag possible abnormalities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, veterinary teams, and boarding staff can use resting pet video to review an estimated respiratory rate, compare it with reference ranges, and check prior monitoring reports. Results are for health reference and do not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only setting may be ignored, and output destination selection may not be respected.

Mitigation: Request fixes and confirm the output destination before use.

Risk: The skill may register cloud accounts and retain credentials; service privacy and retention behavior remain unverified, and pet footage is processed externally.

Mitigation: Request clear account-registration, credential-storage, privacy, retention, and pricing disclosures; use only footage approved for external processing.

## Reference(s):

- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-respiratory-rate-abnormal-detect-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis results, JSON, Markdown]

**Output Format:** [Structured respiratory-rate report; historical reports can be presented as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes estimated breaths per minute and an abnormality alert; intended for resting footage and health reference only, not diagnosis.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
