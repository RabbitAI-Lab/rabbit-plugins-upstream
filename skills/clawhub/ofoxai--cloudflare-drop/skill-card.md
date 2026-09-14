## Description:

cloudflare-drop helps agents publish completed static HTML, CSS, JavaScript, image, and font sites to Cloudflare as verified shareable URLs, using temporary previews without credentials or permanent deployments with Cloudflare credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn a completed static site into a Cloudflare-hosted shareable URL. It supports temporary preview links, permanent account deployments, renewal of archived previews, and optional shared access-code protection for permanent deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload and archive a whole source folder, which may expose unintended sibling files.

Mitigation: Run it from a clean publish folder containing only intended static assets, and keep credentials, private reports, exports, source repositories, and unrelated files outside that folder.

Risk: Temporary deploys are archived locally so expired previews can be renewed.

Mitigation: Treat the local archive as sensitive, configure CLOUDFLARE_DROP_HOME deliberately when needed, and prune old archived artifacts when renewal is no longer required.

Risk: Temporary deployment may move local Wrangler OAuth state, and deployment tooling can change over time.

Mitigation: Review before installing, prefer a narrowly scoped Cloudflare API token for permanent deployments, and use --no-pause-oauth when local Wrangler OAuth state should not be moved.

Risk: Optional six-digit access codes are shared convenience barriers rather than identity or MFA controls.

Mitigation: Use access-code protection only for appropriate low-friction sharing, preserve the -otp flag on protected redeploys, and avoid relying on it for enterprise identity or revocation of already-public copies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/cloudflare-drop)
- [ClawHub metadata homepage](https://github.com/ofoxai/skills/tree/main/skills/cloudflare-drop)
- [OTP security review](references/otp-security.md)
- [Cloudflare Worker-first static assets routing](https://developers.cloudflare.com/workers/static-assets/routing/worker-script/)
- [Cloudflare Durable Object storage](https://developers.cloudflare.com/durable-objects/api/storage-api/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with shell commands and deployment result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report RESULT_URL, MODE, CLAIM_LINK, EXPIRY_EPOCH, OTP_CODE, URL_UNVERIFIED, and renewal status fields depending on deployment outcome.]

## Skill Version(s):

2.3.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
