## Description:

Fast, safe first-run tour of the LAN CLI: discover networks, join a device network, message a peer, share files, and leave cleanly with verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and new LAN CLI users use this skill to complete a first-run onboarding loop for local network discovery, joining, peer messaging, file sharing, verification, and clean exit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Joining unrecognized LAN networks can expose the user to unexpected peers and broadcasts.

Mitigation: Join only networks the user recognizes and leave the network when the onboarding tour is complete.

Risk: Messages and shared files may be visible to other network members.

Mitigation: Do not send secrets or sensitive files, and verify shared state after each action before continuing.

## Reference(s):

- [LAN setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/lan-onboarding-import)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-back verification checkpoints, troubleshooting notes, and safety guidance for local network actions.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
