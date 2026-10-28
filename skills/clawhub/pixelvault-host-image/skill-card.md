## Description:

Uploads a local image or imports an image URL to create a shareable public HTTPS link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[facundofarias](https://clawhub.ai/user/facundofarias)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can upload screenshots, charts, diagrams, or other images and share them in chats, posts, pull requests, or email. Keyless uploads expire after 30 days; an optional API key supports permanent links and URL imports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded images are public to anyone with the link, and imported source URLs are shared with PixelVault.

Mitigation: Upload only images intended for public sharing, and check them for secrets and personal information first.

Risk: An optional API key enables permanent links and should remain private.

Mitigation: Keep PIXELVAULT_API_KEY private and do not print or log it.

## Reference(s):

- [PixelVault OpenClaw integration](https://pixelvault.dev/integrations/openclaw/)
- [PixelVault image API](https://api.pixelvault.dev/v1/images)
- [ClawHub skill page](https://clawhub.ai/facundofarias/skills/pixelvault-host-image)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline curl commands and returned HTTPS image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a public image URL; keyless links expire after 30 days.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
