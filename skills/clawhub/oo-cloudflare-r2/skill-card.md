## Description:

Cloudflare R2 (cloudflare.com). Use this skill for ANY Cloudflare R2 request — reading, creating, updating, and deleting data. Whenever a task involves Cloudflare R2, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cloudflare R2 buckets, objects, CORS policy, and presigned access through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bucket creation, updates, CORS changes, and deletion can expose, alter, or remove Cloudflare R2 resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: Object downloads and presigned URL generation can expose cloud storage data.

Mitigation: Review the requested bucket, object key, URL method, and authorization intent before downloading objects or generating presigned URLs.

Risk: The skill depends on an installed, signed-in oo CLI and a connected Cloudflare R2 account.

Mitigation: Run setup or connection steps only after an action fails with a matching CLI, authentication, connection, or billing error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cloudflare-r2)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cloudflare](https://www.cloudflare.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before running Cloudflare R2 actions.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
