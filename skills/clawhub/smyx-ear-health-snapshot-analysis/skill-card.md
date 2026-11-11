## Description:

Analyzes submitted pet-ear images or videos for visible ear-canal color, discharge, and wax buildup, returning observations, alerts, and suggested follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding centers, and veterinary clinics can use the skill to review visual signs in pet-ear photos or videos and decide whether further examination may be needed. It provides health-reference observations, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account and credential handling and remote destinations are not fully clarified; requests may send credentials to arbitrary destinations.

Mitigation: Avoid installation until credential handling and remote destinations are reviewed and clarified.

Risk: An export-only option may still run analysis.

Mitigation: Clarify export-only behavior before use, and treat the option as potentially running analysis until confirmed.

Risk: Scanner coverage is incomplete, and some imported functionality could not be assessed.

Mitigation: Review the missing local reference and the unassessed imported functionality before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)
- [Pet ear health API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report; Markdown table for history listings; optional JSON or file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual health-reference observations with alerts, follow-up suggestions, and report links; not a diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
