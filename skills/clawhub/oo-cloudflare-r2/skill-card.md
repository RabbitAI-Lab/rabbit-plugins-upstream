## Description:

Cloudflare R2 connector skill for reading, creating, updating, and deleting buckets, objects, account metrics, access settings, custom domains, notifications, lifecycle settings, and related R2 configuration through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cloudflare R2 storage from an agent through OOMOL's connected cloudflare_r2 connector. It supports inspection, object transfer, bucket configuration, temporary access credentials, and user-confirmed write or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes running a remote installer directly in a shell without integrity verification.

Mitigation: Install the oo CLI manually from a trusted, verified installer path and confirm the installer source before use.

Risk: The skill can perform destructive Cloudflare R2 operations, including bucket deletion and object or prefix deletion.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before approving destructive actions.

## Reference(s):

- [ClawHub Cloudflare R2 Skill](https://clawhub.ai/oomol/skills/oo-cloudflare-r2)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cloudflare R2 Homepage](https://www.cloudflare.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses with data and execution metadata when run.]

## Skill Version(s):

1.0.7 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
