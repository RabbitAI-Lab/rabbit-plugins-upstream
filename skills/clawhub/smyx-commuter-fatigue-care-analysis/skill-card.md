## Description:

Analyzes home-arrival living-room camera video to estimate after-work fatigue from posture, facial, and sighing signals, then produces structured care recommendations and optional smart-home comfort actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External smart-home users and integrators use this skill to analyze a consenting user's first 30 minutes after arriving home and generate non-diagnostic fatigue signals, care suggestions, and report links. It is intended for comfort and self-care workflows, not medical diagnosis or employer/insurance monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home camera and optional audio may be processed through cloud services.

Mitigation: Use only after all household members consent, confirm the cloud service provider and retention/deletion controls, and avoid inputs that include non-consenting people.

Risk: The skill can create or reuse account identifiers and persist local tokens in the workspace database.

Mitigation: Review account linkage behavior before installation, restrict workspace access, and confirm local token storage is acceptable for the deployment environment.

Risk: Cloud history and report export links may expose private fatigue or household activity data.

Mitigation: Limit access to report history, validate deletion controls, and avoid sharing generated report links outside the consenting household.

Risk: Fatigue analysis could be mistaken for medical, employment, or insurance assessment.

Mitigation: Present outputs as non-diagnostic comfort guidance only and prohibit use for medical diagnosis, employer monitoring, insurance decisions, or third-party fatigue data sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown or JSON structured analysis report with report links and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save results to a user-specified output file and may include cloud report export links.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
