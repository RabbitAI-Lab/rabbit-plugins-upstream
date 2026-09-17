## Description:

Precoro lets agents operate Precoro through an OOMOL-connected account, inspect live action schemas, and retrieve procurement data such as catalog items, purchase orders, suppliers, users, and warehouses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to work with Precoro procurement records through the OOMOL oo CLI, including listing and retrieving items, purchase orders, suppliers, users, and warehouses. The skill also guides agents to inspect live action schemas before constructing connector requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes mutable remote installer commands that pipe directly into a shell.

Mitigation: Review the CLI installation path before installing; prefer an official package manager, version-pinned download, and checksum or signature verification.

Risk: The connected Precoro account may expose procurement, supplier, user, warehouse, and purchase-order data visible to that account.

Mitigation: Confirm which Precoro account is connected and use the least-privileged account or scopes suitable for the requested task.

Risk: State-changing or destructive connector actions could modify or remove Precoro data if the payload or target is wrong.

Mitigation: Inspect the live action schema first and confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Precoro homepage](https://precoro.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Precoro account before live connector actions can succeed.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
