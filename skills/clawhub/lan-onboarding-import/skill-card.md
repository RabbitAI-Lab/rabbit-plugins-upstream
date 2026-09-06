## Description:

Fast, safe first-run tour of the LAN CLI -- discover networks, join a device network, message a peer, share files, and leave cleanly with verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and new LAN CLI users use this skill to complete a first-run local-network onboarding loop: discover networks, join one, message a peer, share files, verify results, and leave cleanly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LAN traffic and shared content may be visible to other members of the joined local network.

Mitigation: Join only recognized networks, avoid sending secrets or private files, and leave the network when the onboarding loop is complete.

Risk: Installing an untrusted LAN CLI binary could expose the user to local system or network risk.

Mitigation: Install the LAN CLI only from a trusted source before following the onboarding commands.

## Reference(s):

- [LAN setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/lan-onboarding-import)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes verification, troubleshooting, and safety guidance for local-network CLI use.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
