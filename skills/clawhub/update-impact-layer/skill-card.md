## Description:

Before or after OpenClaw updates, track local overwrite risks and bounded integration checks around the native updater.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawsean](https://clawhub.ai/user/clawsean)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw operators and developers use this skill to prepare and verify updates by tracking only local overrides, compatibility obligations, and integrations that the native updater cannot verify.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local impact records may expose private hostnames, account names, installed paths, or internal project links if shared.

Mitigation: Keep private values in the local record and use placeholders in shared materials.

Risk: Updates, repairs, restarts, or recovery cleanup can change a live installation or retire rollback material.

Mitigation: Require the installation owner's explicit approval for mutations, follow the native updater's current guidance, and preview cleanup before accepting the loss of recovery material.

## Reference(s):

- [Local impact layer guidance](references/local-impact-layer.md)
- [Project homepage (skill metadata)](https://github.com/clawSean/update-impact-layer)
- [ClawHub skill page](https://clawhub.ai/clawsean/skills/update-impact-layer)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with update-planning guidance, shell commands, and local impact ledger entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selects only update-relevant local impacts and bounded verification steps.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
