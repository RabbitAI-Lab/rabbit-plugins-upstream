## Description:

Analyzes nighttime video to identify lights-off times and early-morning movement, compare them with a personal baseline, and report possible sleep-rhythm changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families and community care workers can use the skill to review nighttime routine trends for a person living alone and decide when to check in. Its results are visual observations and deviation alerts, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private video may still be submitted when export-only mode is selected.

Mitigation: Confirm informed consent, processing scope, charges, and retention/deletion terms before use; do not treat export-only mode as a privacy control.

Risk: Credential handling lacks adequate safeguards.

Mitigation: Request fixes that restrict where credentials can be sent and protect token storage before connecting an account.

Risk: The package is not sufficient for continuous safety monitoring.

Mitigation: Use alerts only to prompt human check-ins and do not rely on the package alone for ongoing safety monitoring.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis report or historical report list with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual routine observations and deviation alerts; no medical diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
