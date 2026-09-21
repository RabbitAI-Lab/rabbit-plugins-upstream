## Description:

Uses the OOMOL oo CLI to inspect App Store Server API action schemas and run App Store Server API read, write, and destructive workflows through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app operations teams use this skill to query App Store Server API data, inspect live connector schemas, and run account actions such as subscription, transaction, refund, notification, retention messaging, and renewal-date workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes one-line remote installer commands.

Mitigation: Use OOMOL's manual or verified CLI installation path before installing the oo CLI.

Risk: The skill can perform high-impact App Store Server API changes, including write and destructive actions.

Mitigation: Confirm the exact target account, environment, product, transaction, subscription, and payload before allowing write or destructive actions to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-app-store-server)
- [Apple App Store Server API documentation](https://developer.apple.com/documentation/appstoreserverapi)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command responses are expected as JSON from the oo CLI when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
