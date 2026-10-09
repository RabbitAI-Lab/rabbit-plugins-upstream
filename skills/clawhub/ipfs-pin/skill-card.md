## Description:

Manages local IPFS file pinning, retrieval, and time-based cleanup through an OpenClaw skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paradoxfuzzle](https://clawhub.ai/user/paradoxfuzzle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users add files to a local IPFS node, keep active content pinned, retrieve it by CID, and clean up expired pins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Files added to IPFS may be addressable by CID through the local node.

Mitigation: Do not add private files unless CID-addressable access is intended.

Risk: Removing pins or running TTL-based decay and repository garbage collection may remove locally retained content.

Mitigation: Review TTL settings and preview expiration with decay --dry-run before cleanup.

## Reference(s):

- [Ipfs Pin Stage on ClawHub](https://clawhub.ai/paradoxfuzzle/skills/ipfs-pin)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Plain text or JSON with CLI-reported CIDs and status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local IPFS CLI and reachable node; default pin TTL is 72 hours.]

## Skill Version(s):

0.1.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
