## Description:

Evervault (evervault.com). Use this skill for ANY Evervault request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Evervault connector actions through an OOMOL-connected account, including JSON encryption, JSON decryption, and token metadata inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Encrypt and decrypt actions may expose or transform sensitive Evervault data.

Mitigation: Review the exact action payload and expected effect with the user before running write-tagged Evervault actions.

Risk: First-time setup may require running remote oo CLI installer commands.

Mitigation: Run installer commands only when the CLI is missing and only after confirming the user trusts OOMOL's CLI distribution path.

Risk: The skill routes Evervault work through OOMOL as a connector intermediary.

Mitigation: Use the skill only when the user is comfortable using an OOMOL-connected account for Evervault data.

## Reference(s):

- [Evervault homepage](https://evervault.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-evervault)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo connector, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
