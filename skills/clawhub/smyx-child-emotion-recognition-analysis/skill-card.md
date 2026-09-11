## Description:

Identifies negative emotions such as crying, anger, fear, and distress through surveillance footage, then returns structured analysis and caregiver-facing alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, daycare operators, and developers use this skill to analyze child images, videos, or video URLs for negative emotional states and to retrieve structured historical reports. Results are decision support only and should not replace adult supervision or emergency response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive child media and report data through remote analysis services.

Mitigation: Use only approved data with appropriate consent, force HTTPS production endpoints, and confirm retention and deletion practices before processing real children's images, video, audio, or reports.

Risk: Default configuration and service behavior include cleartext endpoints and payment redirection paths.

Mitigation: Review configuration before installation, remove or neutralize payment redirection behavior, and reject non-HTTPS endpoint settings for real deployments.

Risk: The skill creates or reuses local identity, token, report, and database records.

Mitigation: Review how local records are created, stored, retained, and deleted, and keep internal identity values out of user-facing outputs.

Risk: Dependency names and runtime configuration may need correction before reliable installation.

Mitigation: Validate dependencies and configuration in a test environment before installing into a shared or production agent workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [API interface document](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON text with optional output files and report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list historical reports and can save generated analysis output to a user-specified file.]

## Skill Version(s):

1.0.26 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
