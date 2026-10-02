## Description:

Analyzes nighttime crib footage for infant blanket coverage and kicking or blanket-slippage events, returning reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers of infant-monitoring tools can analyze nighttime crib footage to review blanket coverage, kicking events, alerts, and historical reports. The results are visual observations, not medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant and home-monitoring footage or video URLs are sent to a cloud service.

Mitigation: Obtain explicit consent before analysis and share only footage appropriate for cloud processing.

Risk: The skill may create or reuse an account identity, store tokens locally, and retrieve historical reports without a separate prompt.

Mitigation: Confirm before accessing reports, restrict access to local tokens, and review account and retention settings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown report with alerts, coverage observations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a cloud-hosted historical report list.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
