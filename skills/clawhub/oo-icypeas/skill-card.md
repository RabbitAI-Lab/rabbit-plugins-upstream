## Description:

Icypeas lets agents operate Icypeas through an OOMOL-connected account to read, create, and update data with the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Icypeas action schemas and run email discovery, email verification, reverse email lookup, domain scan, search status, and subscription credit actions through OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Review the installation path first and prefer an official package manager or a versioned installer with checksum or signature verification.

Risk: Connector write actions can change Icypeas account state or consume credits.

Mitigation: Confirm the exact payload, expected account impact, and billing implications before running write actions.

Risk: Connector actions depend on live schemas and OOMOL-managed credentials.

Mitigation: Inspect the live action schema before constructing payloads and fall back to setup only after authentication, connection, scope, or billing errors.

## Reference(s):

- [Icypeas homepage](https://www.icypeas.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-icypeas)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke oo CLI connector actions that return JSON responses from Icypeas.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
