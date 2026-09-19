## Description:

TelTel helps agents operate TelTel through the OOMOL oo CLI for account balance checks, SMS delivery report retrieval, and outbound SMS sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to interact with a connected TelTel account through OOMOL, including checking account balance, reviewing SMS delivery reports, and sending outbound SMS after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Use a verified or package-managed oo CLI installation path when available, and do not run pipe-to-shell or irm-to-iex commands blindly.

Risk: The send_sms action changes TelTel state and may affect account usage or billing.

Mitigation: Confirm the exact outbound SMS payload and effect with the user before running the action.

Risk: Commands may fail when the oo CLI is not installed, the user is not signed in, the TelTel connection is missing or expired, or account credit is insufficient.

Mitigation: Follow the documented setup and billing recovery steps only after a matching command failure occurs.

## Reference(s):

- [TelTel homepage](https://www.teltel.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the oo CLI to inspect live action schemas and run TelTel connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
