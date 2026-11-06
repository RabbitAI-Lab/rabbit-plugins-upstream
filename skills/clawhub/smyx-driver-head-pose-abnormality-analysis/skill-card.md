## Description:

Analyzes submitted in-cabin driver recordings for head-down and side-view posture patterns and returns structured results and historical report information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fleet teams use the skill to submit in-cabin recordings for driver head-pose analysis and retrieve prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted driver recordings may be uploaded to a remote service, including when using the export-only option.

Mitigation: Confirm export-only behavior before use, obtain permission to upload footage, and check the provider's retention and deletion terms.

Risk: Credential handling is unsafe, and the configured API destination may not be controlled by --api-url.

Mitigation: Keep API secrets separate from identity fields, use clear account and token controls, and verify the destination before uploading recordings.

Risk: Live driving-alert claims exceed the supplied implementation, and remote service behavior is unverified.

Mitigation: Treat results as cloud analysis of submitted recordings; do not rely on the skill for live driving warnings.

## Reference(s):

- [Driver head-pose API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured analysis results and Markdown report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report content depends on the submitted recording and available history.]

## Skill Version(s):

1.0.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
