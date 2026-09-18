## Description:

Courier enables agents to operate Courier through an OOMOL-connected oo CLI for reading, creating, updating, and deleting profiles, subscription lists, and messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Courier user profiles, subscription lists, and message sends through OOMOL-brokered Courier connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup directs users to run remote installer scripts directly in a shell.

Mitigation: Prefer a verified, versioned installer with checksums or signatures and review the installer payload before execution.

Risk: State-changing Courier actions can alter profiles, subscription lists, or message delivery.

Mitigation: Confirm the exact payload and intended effect with the user before write actions.

Risk: Destructive Courier actions can delete profiles, delete lists, or unsubscribe list members.

Mitigation: Require explicit approval for the target object and destructive action before execution.

Risk: Courier operations are brokered through OOMOL-connected credentials.

Mitigation: Use this skill only when the operator trusts OOMOL to broker Courier access.

## Reference(s):

- [Courier homepage](https://www.courier.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
