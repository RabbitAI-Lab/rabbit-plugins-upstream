## Description:

Helps an agent operate OneSignal through an OOMOL-connected account for reading messages, creating push notifications, and canceling scheduled messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect OneSignal action schemas and run OOMOL connector actions to list, retrieve, create, or cancel OneSignal messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer guidance includes remote shell commands for the oo CLI.

Mitigation: Review the installer path and prefer official, versioned, verifiable oo CLI installation instructions before installation.

Risk: Write actions can create push notifications or cancel scheduled messages.

Mitigation: Confirm the exact OneSignal payload and effect with the user before approving write actions.

## Reference(s):

- [OneSignal homepage](https://onesignal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-onesignal-rest-api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI and receive JSON connector responses when actions are run.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
