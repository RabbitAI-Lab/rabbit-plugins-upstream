## Description:

This skill lets agents handle eSignatures.com requests for reading, creating, and updating templates and contracts through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage eSignatures.com templates and contracts through an OOMOL-connected account. It supports reading templates and contracts, creating templates or contracts, retrieving Markdown contract content, and withdrawing contracts when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute a remote installer in the shell without verification.

Mitigation: Review the setup path before installing, prefer a verified official package or inspected installer, and avoid running the remote installer blindly.

Risk: Contract and template creation or withdrawal can change eSignatures.com account state.

Mitigation: Inspect the live action schema first and confirm the exact payload, target, and effect with the user before running write or withdrawal actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esignatures-io)
- [eSignatures.com homepage](https://esignatures.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return eSignatures.com data and Markdown contract content through oo CLI JSON responses; write and withdrawal actions require exact user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
