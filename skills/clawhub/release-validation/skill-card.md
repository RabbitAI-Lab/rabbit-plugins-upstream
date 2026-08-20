## Description:

Safely copy an existing gateway, upgrade it to an OpenClaw beta, and guide human release testing with one Markdown worksheet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openclaw](https://clawhub.ai/user/openclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release testers use this skill to initialize or join an OpenClaw beta validation campaign, create an isolated upgraded gateway copy, record manual test findings in a Markdown worksheet, and publish consolidated feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitHub credentials to read, create, label, close, and comment on OpenClaw release-validation issues.

Mitigation: Use an account with appropriate repository access, review the campaign issue and final feedback before publication, and avoid running the workflow where GitHub credentials should not be available.

Risk: The skill copies a selected OpenClaw gateway, including sessions and local state, into a disposable test environment.

Mitigation: Choose the source gateway deliberately, prefer a non-sensitive source when possible, and destroy or retain the disposable environment only after reviewing the validation result.

Risk: The workflow may install OCM and run OpenClaw upgrade commands on the copied gateway.

Mitigation: Review the OCM install prompt, approve installation only when intended, and keep upgrade testing scoped to the isolated copied environment.

## Reference(s):

- [OpenClaw Release Validation on ClawHub](https://clawhub.ai/openclaw/skills/release-validation)
- [OpenClaw maturity scorecard](https://docs.openclaw.ai/maturity/scorecard.md)
- [OpenClaw documentation](https://docs.openclaw.ai)
- [Validation worksheet template](artifact/assets/validation-worksheet.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown worksheet, concise text updates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single editable validation worksheet and a consolidated release-feedback comment.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
