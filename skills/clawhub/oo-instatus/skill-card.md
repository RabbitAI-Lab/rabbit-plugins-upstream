## Description:

Enables agents to manage Instatus status pages, components, incidents, and incident updates through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect and manage Instatus status pages, components, incidents, and incident updates from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include running a remote installer directly in the shell without integrity checks or explicit approval.

Mitigation: Before installing, review the OOMOL CLI installer source or use a safer installation path from the vendor.

Risk: Write actions can change Instatus components, incidents, or incident updates.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Destructive actions can delete Instatus components, incidents, or incident updates.

Mitigation: Confirm the target resource and obtain explicit user approval before running destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-instatus)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Instatus](https://instatus.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, authenticated OOMOL account, and connected Instatus provider before actions can run.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
