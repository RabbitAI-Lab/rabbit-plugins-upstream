## Description:

Publish a static site to Cloudflare and return a verified live URL, using permanent account deploys when Cloudflare credentials are present or 60-minute claimable previews when they are not.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to publish finished static HTML/CSS/JS/image sites as shareable Cloudflare Workers URLs. It is suited for reports, mockups, one-off landing pages, and other static web deliverables that need a verified public link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish local static-site files to a public Cloudflare URL, including unintended private files if run from an unsafe directory.

Mitigation: Run it only from a clean, dedicated static-site folder and review the content before publishing.

Risk: Temporary preview URLs expire after about 60 minutes and can be mistaken for permanent links.

Mitigation: State the deployment mode and expiry when sharing a URL; use a Cloudflare API token for permanent deploys or claim the preview when persistence is required.

Risk: The temporary deploy path may move local Wrangler OAuth state during deployment.

Mitigation: Prefer an explicit Cloudflare API token for permanent deploys, or use --no-pause-oauth when OAuth state should not be touched.

Risk: The deploy index can retain deployed HTML and claim links under ~/.cloudflare-drop.

Mitigation: Review or prune the deploy index periodically, and use CLOUDFLARE_DROP_HOME to keep records in a dedicated location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/cloudflare-drop)
- [Source homepage](https://github.com/ofoxai/skills/tree/main/skills/cloudflare-drop)
- [Deployment command](references/deploy.mjs)
- [Wrangler deployment helper](references/wrangler.mjs)
- [TTL handling](references/ttl.mjs)
- [Deployment index](references/drop-index.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and deployment result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or renews public Cloudflare Workers URLs, reports the deployment mode and expiry, and falls back to the local file when URL verification fails.]

## Skill Version(s):

2.2.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
