## Description:

Enables agents to read, create, update, and delete Cloudflare R2 data through the OOMOL-connected oo CLI instead of calling the Cloudflare R2 API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Cloudflare R2 connector schemas and run validated bucket, object, domain, lifecycle, CORS, object lock, upload, Sippy, event notification, metrics, and pre-signed URL actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloudflare R2 metadata and some object contents may route through OOMOL's third-party connector.

Mitigation: Install and use the skill only when that routing is acceptable, and grant the Cloudflare connector the narrowest permissions needed for the task.

Risk: The skill can perform write and destructive storage operations such as deleting buckets, objects, domains, event rules, or policies.

Mitigation: Confirm the exact target, payload, and effect with the user before any write action, and require explicit approval before destructive actions.

Risk: The documented setup path includes remote installer commands.

Mitigation: Avoid running remote installer commands unless the installer source has been independently trusted and verified.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cloudflare-r2)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cloudflare R2 Homepage](https://www.cloudflare.com)
- [OOMOL Cloudflare R2 Connection](https://console.oomol.com/app-connections?provider=cloudflare_r2)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector action schemas before constructing action payloads; state-changing and destructive actions require user confirmation.]

## Skill Version(s):

1.0.9 (source: server evidence release version and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
