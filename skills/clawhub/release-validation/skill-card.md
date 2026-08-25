## Description:

Safely copy an existing gateway, test the latest OpenClaw main commit, and guide human release-campaign feedback with one Markdown worksheet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openclaw](https://clawhub.ai/user/openclaw)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw maintainers and testers use this skill to validate a release campaign against a copied real gateway, record manual surface-test notes, and prepare sanitized feedback for a shared GitHub issue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can use GitHub permissions and publish release-validation feedback.

Mitigation: Use it only for OpenClaw release validation and review the generated report draft before approving publication.

Risk: The workflow copies a selected local gateway into a disposable test environment.

Mitigation: Confirm the gateway selection and rely on the disposable copy; the source gateway is not modified.

Risk: Copied channel credentials can conflict with the source gateway while the test copy runs.

Mitigation: Temporarily stop the current credential owner before activating the copy and restore it when validation ends.

Risk: Optional diagnostics can capture local traces, metrics, and logs from the disposable test gateway.

Mitigation: Keep diagnostics opt-in, loopback-only, bounded, and local; review and redact any diagnostic evidence before it appears in a report.

## Reference(s):

- [Structured release report contract](references/structured-report.md)
- [OpenClaw maturity scorecard](https://docs.openclaw.ai/maturity/scorecard.md)
- [OpenClaw documentation](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, worksheet updates, and release-report drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a private worksheet, a reviewable GitHub release-feedback draft, and optional local diagnostic summaries.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
