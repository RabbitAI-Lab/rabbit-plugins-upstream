## Description:

Analyzes in-cabin driver face video to report eye state, blink rate, eye-closure duration, fatigue level, warnings, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, fleet operators, and developers use this skill to submit driver-facing DMS video or URLs for visual fatigue indicators such as blink rate, eye-closure duration, microsleep events, PERCLOS, fatigue level, and suggested safety actions. The output is an auxiliary safety report and should not be treated as a medical or sleep-disorder diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver-facing video can contain biometric and identity-linked information and may be uploaded to third-party backend services.

Mitigation: Use only with informed driver or employee consent, confirm that cloud processing and report retention are allowed for the deployment, and follow applicable privacy requirements.

Risk: The skill can create or reuse a cloud identity automatically and associate historical reports with that identity.

Mitigation: Review identity handling before deployment, disclose account association to affected users, and restrict historical report access to authorized operators.

Risk: Cloud access tokens may be stored in the local workspace database.

Mitigation: Protect workspace data directories, rotate or revoke tokens if a workspace is shared or exposed, and remediate local token persistence before sensitive deployments.

Risk: Fatigue alerts depend on camera quality and visibility of the driver's eyes.

Mitigation: Require a suitable DMS camera view, adequate lighting or infrared support, stable visibility of both eyes, and human review of warnings before operational action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON structured analysis report with fatigue metrics, warning messages, recommended actions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a local file when an output path is provided.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
