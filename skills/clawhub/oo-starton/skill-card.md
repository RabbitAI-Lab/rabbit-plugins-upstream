## Description:

Starton lets agents operate Starton IPFS pin workflows through the OOMOL-connected starton connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to list, read, create, pin, and delete Starton IPFS pins from a connected OOMOL account while checking live connector schemas before action execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports unsafe remote installer commands in the first-time setup path.

Mitigation: Before installation, require safer oo CLI installation steps or manually verify the installer.

Risk: The security evidence reports that pin_existing_file creates a Starton pin but is not clearly labeled as a write action.

Mitigation: Treat pin_existing_file as a write action and confirm the exact payload and expected effect with the user before running it.

Risk: The skill can create and delete Starton project pins through a connected account.

Mitigation: Require confirmation for writes and explicit approval of destructive delete targets before running connector actions.

## Reference(s):

- [ClawHub Starton skill page](https://clawhub.ai/oomol/skills/oo-starton)
- [Starton homepage](https://starton.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON data and execution IDs from Starton actions.]

## Skill Version(s):

1.0.4 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
