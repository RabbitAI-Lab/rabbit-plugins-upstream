## Description:

Cloudflare R2 agent skill for listing accounts and buckets, managing buckets and CORS policies, handling object transfers, and generating presigned URLs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cloudflare R2 storage through an OOMOL-connected account, including bucket administration, CORS policy management, object upload and download, and presigned URL generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can execute a remote oo CLI installer script.

Mitigation: Review the official install instructions or verify the installer before execution, and run it only when the publisher and installer source are trusted.

Risk: Bucket, CORS, and object actions can change or delete Cloudflare R2 resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: Connector actions depend on the authenticated OOMOL account and connected Cloudflare R2 credential.

Mitigation: Use the live connector schema before constructing payloads and limit actions to the intended account, bucket, and object scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-r2)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Cloudflare R2](https://www.cloudflare.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.6 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
