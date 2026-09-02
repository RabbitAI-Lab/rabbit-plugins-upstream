## Description:

Test the latest OpenClaw main commit through an isolated OCM copy or an explicitly approved in-place gateway update, then guide structured release feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openclaw](https://clawhub.ai/user/openclaw)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw release testers use this skill to validate a selected gateway against the latest main commit, record manual surface-testing notes, and prepare sanitized release feedback for the shared campaign issue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: In-place validation can modify a real selected OpenClaw gateway.

Mitigation: Prefer the isolated OCM copy path; use in-place mode only after the tester reviews the dry run and explicitly approves the update.

Risk: Release feedback may be posted publicly to GitHub.

Mitigation: Draft and sanitize proposed posts locally, then publish only after explicit user approval.

Risk: Tooling, diagnostics, or gateway evidence may contain sensitive local details.

Mitigation: Keep tooling packets and telemetry private, redact local identifiers and raw logs, and exclude setup or cleanup details from public release feedback.

## Reference(s):

- [OpenClaw Release Validation on ClawHub](https://clawhub.ai/openclaw/skills/release-validation)
- [Structured release report contract](references/structured-report.md)
- [Tooling-feedback packet procedure](references/tooling-feedback.md)
- [OpenClaw maturity scorecard](https://docs.openclaw.ai/maturity/scorecard.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown worksheets and reports, JSON campaign artifacts, shell commands, and concise guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Human review and explicit approval are required before public GitHub posting or in-place gateway updates.]

## Skill Version(s):

0.1.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
