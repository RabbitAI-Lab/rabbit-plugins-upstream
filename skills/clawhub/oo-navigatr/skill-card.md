## Description:

Uses the OOMOL-connected oo CLI to retrieve and manage Navigatr badges and badge assertions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Navigatr users can retrieve badges and issuance records, issue badges, and revoke or verify badge assertions through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Navigatr through OOMOL grants a broker access to account data.

Mitigation: Confirm that using OOMOL as the broker is acceptable before connecting the account.

Risk: Issuing, revoking, or verifying assertions can change badge records or public verification status.

Mitigation: Inspect the live action schema and confirm the exact target, payload, and effect with the user before state-changing actions.

Risk: First-time setup instructions include commands that execute downloaded installer scripts.

Mitigation: Prefer OOMOL's official installation documentation or verify installer sources before running those commands.

## Reference(s):

- [Navigatr skill on ClawHub](https://clawhub.ai/oomol/skills/oo-navigatr)
- [Navigatr](https://www.navigatr.org)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with CLI commands and retrieved badge data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected account's access and the selected action.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
