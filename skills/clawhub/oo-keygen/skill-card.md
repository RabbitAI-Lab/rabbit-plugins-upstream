## Description:

Keygen (keygen.sh) supports Keygen requests that read, create, update, or delete account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Keygen products, policies, licenses, users, groups, entitlements, machines, components, processes, validations, usage, and heartbeats through OOMOL's Keygen connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports unsafe installer instructions for the oo CLI.

Mitigation: Avoid pipe-to-shell installation unless the oo CLI source is independently trusted and verified; prefer the documented install guide or an approved package source.

Risk: The skill can change or delete important Keygen account data.

Mitigation: Require explicit user confirmation for operations that create, update, delete, revoke, suspend, renew, reset, attach, detach, or otherwise change licenses, users, products, policies, machines, usage, or relationships.

Risk: The security review says some state-changing actions are under-disclosed as safe reads.

Mitigation: Inspect each live action schema and action name before execution, and treat untagged relationship, heartbeat, usage, renewal, suspension, revocation, and ownership changes as requiring confirmation.

## Reference(s):

- [Keygen homepage](https://keygen.sh)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-keygen)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses live action schemas before constructing Keygen connector payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
