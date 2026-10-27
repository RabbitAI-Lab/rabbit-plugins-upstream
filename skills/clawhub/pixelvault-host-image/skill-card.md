## Description:

Turn a local image file, or an image URL, into a public https link with one curl call. Use when you need a shareable URL for a screenshot, chart, generated image, or diagram, for example to send it in chat, embed it in a post, a PR, or an email. Works with no signup or API key (temporary link, 30 days); add PIXELVAULT_API_KEY for permanent links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[facundofarias](https://clawhub.ai/user/facundofarias)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can upload a local image, or import an image from a URL with an API key, to get a shareable public HTTPS link for use in chat, posts, code reviews, email, or web pages. Keyless uploads create temporary links that expire after 30 days; keyed uploads can be permanent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploads are publicly shareable and may expose secrets or personal information contained in an image.

Mitigation: Review images for secrets and personal information before upload, including images imported from a URL; keep PIXELVAULT_API_KEY private.

## Reference(s):

- [PixelVault OpenClaw integration](https://pixelvault.dev/integrations/openclaw)
- [PixelVault Images API](https://api.pixelvault.dev/v1/images)
- [PixelVault Dashboard](https://pixelvault.dev/dashboard/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [A public HTTPS image URL returned as text, with Markdown guidance and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keyless links expire after 30 days; keyed uploads can be permanent. Hosted images are public to anyone with the link. Free-plan uploads are limited to 5 MB and supported image formats.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
