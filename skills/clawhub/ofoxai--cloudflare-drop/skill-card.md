## Description:

cloudflare-drop publishes a finished static site to Cloudflare as a verified shareable URL, using permanent deployments when credentials are available or 60-minute claimable previews otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to publish static HTML, CSS, JavaScript, image, and font assets to a live Cloudflare URL, with deployment mode reporting and verification before the link is shared. It is suited to reports, mockups, one-off landing pages, and AI-generated static sites that need a temporary preview or an authenticated permanent deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default staging behavior can publish extra sibling files from the same folder after warning about them.

Mitigation: Publish from a clean, dedicated folder, read STAGED_REVIEW before sharing a URL, and use --assets-only for ordinary static pages when unrelated files should be skipped.

Risk: Cloudflare credentials and permanent deployments can persist beyond the current session.

Mitigation: Use narrowly scoped Cloudflare tokens and choose temporary previews when a short-lived share is sufficient.

Risk: Private reports, database backups, credentials, source trees, or unrelated exports may become public if staged beside the HTML deliverable.

Mitigation: Keep sensitive and unrelated files outside the publish folder, and relay any STAGED_REVIEW warnings before distributing a deployment link.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/cloudflare-drop)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/cloudflare-drop)
- [OTP security review](references/otp-security.md)
- [Cloudflare Workers static assets routing](https://developers.cloudflare.com/workers/static-assets/routing/worker-script/)
- [Cloudflare Durable Object storage](https://developers.cloudflare.com/durable-objects/api/storage-api/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with inline shell commands and deployment result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include RESULT_URL, MODE, CLAIM_LINK, EXPIRY_EPOCH, and OTP_CODE when those values are produced by a verified deployment.]

## Skill Version(s):

2.4.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
