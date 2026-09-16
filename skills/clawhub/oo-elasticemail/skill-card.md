## Description:

Operate Elastic Email through the OOMOL oo CLI connector for reading, creating, updating, and deleting contacts and contact lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Elastic Email contact and list workflows through an OOMOL-connected account. It supports read actions and confirmed write or destructive actions for contacts, lists, and list membership.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents curl-to-bash and PowerShell remote installer commands that may execute unverified code.

Mitigation: Review the skill before installing, avoid elevated/admin shells for those installer commands, and prefer a verified, versioned CLI install path with checksum or signature validation.

Risk: The skill can perform write and destructive Elastic Email actions, including contact deletion, list deletion, and membership removal.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any action tagged write or destructive.

Risk: Elastic Email credentials are mediated server-side by OOMOL.

Mitigation: Use this skill only when the user trusts OOMOL to mediate Elastic Email actions and handle connected credentials server-side.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Elastic Email homepage](https://elasticemail.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should fetch the live connector schema before constructing payloads and should surface execution results returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
