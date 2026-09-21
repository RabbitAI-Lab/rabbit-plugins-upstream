## Description:

Cloudflare R2 helps agents operate Cloudflare R2 through OOMOL's oo CLI for reading, creating, updating, and deleting storage resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cloudflare R2 buckets, objects, access settings, domains, lifecycle rules, CORS, locks, metrics, notifications, temporary credentials, presigned URLs, and related background jobs from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may pipe a remote installer directly into a shell.

Mitigation: Review the OOMOL CLI installer before running it and prefer a verified package or signed release when available.

Risk: The skill can change or delete Cloudflare R2 storage data.

Mitigation: Confirm the exact bucket, object, action, and payload before allowing write or destructive operations.

Risk: Connector action payloads may drift from the skill text.

Mitigation: Inspect the live connector schema before constructing or running an action payload.

## Reference(s):

- [Cloudflare R2 homepage](https://www.cloudflare.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-r2)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and returns connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
