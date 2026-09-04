## Description:

Fast, safe first-run tour of the LAN CLI: discover networks, join a device network, message a peer, share files, and leave cleanly with verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to complete a first-run LAN CLI onboarding loop: discover local networks, join one, exchange a message, share files, verify results, and leave cleanly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted LAN CLI binary could expose the user to unsafe local execution.

Mitigation: Install the lan CLI only from a trusted source before following the onboarding steps.

Risk: LAN traffic and shared files are visible to network members.

Mitigation: Join only recognized networks and avoid sending secrets or publishing private files.

Risk: Continuing after an unverified join, message, or file operation could lead to mistaken assumptions about network state.

Mitigation: Follow the skill's read-back verification loop after each action and leave and rejoin if verification fails.

## Reference(s):

- [LAN setup](references/setup.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes verification, safety, and troubleshooting steps for a local-first LAN CLI tour.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
