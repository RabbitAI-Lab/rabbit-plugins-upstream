## Description:

PassSlot (passslot.com) lets an agent read, create, update, and delete PassSlot Wallet pass data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage PassSlot Wallet passes through an OOMOL-connected account, including listing pass assets, creating passes from templates, updating placeholder values, retrieving installation URLs, and deleting passes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run internet-downloaded oo CLI installer scripts.

Mitigation: Review the installer path before installation and prefer a package-manager or version-pinned installer with checksum or signature verification.

Risk: PassSlot write actions can create or update Wallet pass data.

Mitigation: Confirm the exact target payload and expected effect with the user before running actions tagged as write.

Risk: The destructive delete action can permanently remove PassSlot Wallet passes.

Mitigation: Confirm the pass target and require explicit user approval before running destructive deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-passslot)
- [PassSlot homepage](https://www.passslot.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return PassSlot pass data, placeholder values, execution IDs, and installation URLs from oo CLI connector responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
