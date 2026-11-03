## Description:

Analyzes submitted pet ear images or video for visible redness, discharge, and wax buildup, then returns observations and suggested veterinary follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding staff, and veterinary teams can use the skill to review pet ear imagery for visible changes and organize preliminary observations. It provides informational observations and follow-up suggestions, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that upload and destination controls do not work, which may prevent private footage from being handled as intended.

Mitigation: Wait for fixes to the export-only and destination controls before submitting private footage.

Risk: Automatic account creation and local token storage create privacy risks around account and credential handling.

Mitigation: Review automatic account creation and local token storage; avoid supplying sensitive credentials until secrets are separated from account identifiers.

Risk: Media retention, deletion terms, and service charges need review before use.

Mitigation: Review the service's media retention and deletion terms and any applicable charges before submitting footage.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON analysis report; Markdown history report list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes visible ear observations, abnormality alerts, suggested follow-up, and report links; it is not a diagnosis.]

## Skill Version(s):

1.0.13 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
