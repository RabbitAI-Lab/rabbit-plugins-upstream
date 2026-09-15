## Description:

BaseLinker helps agents operate BaseLinker account data through the OOMOL-connected oo CLI for reading, creating, and updating BaseLinker records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect BaseLinker connector schemas, run inventory and order-management actions through the oo CLI, and get setup guidance when authentication, connection, or billing errors block use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Review the oo CLI installation path before installation, prefer a verified or pinned package with checksums or signatures, and do not let an agent run the remote installer automatically.

Risk: Some BaseLinker actions are tagged as write actions, including order event and order status listing actions whose side effects are unclear in the documentation.

Mitigation: Confirm any write-tagged action and its exact payload with the user before execution.

## Reference(s):

- [BaseLinker homepage](https://baselinker.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-baselinker)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should inspect live action schemas before constructing payloads and should confirm user intent before write-tagged or destructive actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
