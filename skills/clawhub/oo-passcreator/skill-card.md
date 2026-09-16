## Description:

Passcreator helps agents operate Passcreator through an OOMOL-connected account using the oo CLI for pass creation, template inspection, and pass listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Passcreator wallet-pass workflows from an agent, including creating passes from template-specific JSON data and reading templates or existing passes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review the oo CLI installation path first and prefer an official package manager, signed release, or installer with checksum or signature verification.

Risk: The create_pass action changes Passcreator account state.

Mitigation: Confirm the exact create_pass payload and expected effect with the user before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-passcreator)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Passcreator homepage](https://www.passcreator.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions should be confirmed before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
