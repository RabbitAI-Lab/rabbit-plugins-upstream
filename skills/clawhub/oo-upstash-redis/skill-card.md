## Description:

Use this skill to operate Upstash Redis through an OOMOL-connected account for reading, creating, updating, and deleting Redis data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live connector schemas and run Upstash Redis key operations through the OOMOL oo CLI, including read, write, expiration, scan, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup commands execute downloaded installer scripts directly.

Mitigation: Install the oo CLI from a verified, versioned source and validate checksums or signatures before use.

Risk: Redis write and destructive actions can change expiration settings, overwrite values, or delete keys.

Mitigation: Confirm the exact key, payload, and intended effect before running actions tagged as write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-upstash-redis)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Upstash Redis homepage](https://upstash.com/redis)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions should fetch the live action schema before constructing payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
