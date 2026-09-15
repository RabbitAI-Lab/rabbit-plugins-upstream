## Description:

Vestaboard lets an agent read, create, and update Vestaboard content through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to operate a connected Vestaboard account, including reading the current message, sending messages, and updating transition settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run remote installer scripts for the oo CLI.

Mitigation: Use a verified installation path, such as a signed package or fixed release, or review and checksum downloaded scripts before execution.

Risk: Write actions can change the displayed Vestaboard message or transition settings.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

Risk: The skill depends on OOMOL-managed credentials and connector availability.

Mitigation: Use the skill only when the user trusts OOMOL and has connected Vestaboard through the OOMOL account connection flow.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Vestaboard homepage](https://www.vestaboard.com)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vestaboard)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with oo CLI commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should fetch the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
