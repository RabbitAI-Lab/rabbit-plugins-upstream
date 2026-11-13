## Description:

Analyzes supplied child-bedroom audio and video for signs of bedtime distress and returns structured findings, suggested responses, or report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers can use the skill to review child-bedroom recordings for crying, fear-related behavior, or nightmare awakenings and receive a structured report. Use requires careful handling of sensitive recordings and independent caregiver judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private bedroom recordings may be uploaded for remote processing even when an export-only option is selected.

Mitigation: Review the workflow and obtain clear approval for remote processing before supplying recordings; do not treat export-only as a privacy boundary.

Risk: The bundled code does not establish automatic soothing or urgent caregiver alerts, and provider retention and device-action delivery are unverified.

Mitigation: Treat reports as advisory and do not rely on automatic soothing or urgent alerts; verify retention and delivery before any care workflow depends on them.

Risk: Local authentication tokens persist in the workspace database, and credential and identity fields require separation.

Mitigation: Review token storage and separate credentials from identity fields before installation or use.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report in JSON or Markdown, with findings, suggestions, and report links where returned by the service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output details depend on the service response.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
