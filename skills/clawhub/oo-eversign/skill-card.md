## Description:

Operates Xodo Sign through an OOMOL-connected account to read, create, and update signing documents, templates, audit logs, businesses, signers, and reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to operate Xodo Sign workflows through the OOMOL-connected oo CLI, including document creation, template-based sending, audit lookup, signer reassignment, reminders, and list or retrieval operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes remote installer commands that could execute unverified code.

Mitigation: Install the oo CLI through a verified, version-pinned method, or inspect and verify the installer before running it.

Risk: Write actions can change real Xodo Sign signing workflows, including creating documents, reassigning signers, and sending reminders.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any write action.

## Reference(s):

- [Xodo Sign homepage](https://eversign.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-eversign)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
