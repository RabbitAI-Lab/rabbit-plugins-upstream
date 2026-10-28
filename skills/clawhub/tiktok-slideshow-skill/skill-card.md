## Description:

Plans, writes, and renders TikTok photo slideshows for app marketing, supports confirmed publishing to TikTok and Instagram, and reviews performance to guide follow-up tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[social-media-skills](https://clawhub.ai/user/social-media-skills)

### License/Terms of Use:

MIT-0

## Use Case:

App founders and indie hackers use this skill to create and test honest marketing slideshows for their apps on TikTok and Instagram, including rendering, confirmed publishing, and performance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WoopSocial connection credentials, especially API keys placed in URLs, could be exposed.

Mitigation: Prefer OAuth; if an API-key URL is necessary, protect the configuration, redact it from logs, and rotate any exposed key.

Risk: The slide renderer may download a font automatically.

Mitigation: Use a reviewed local font through the renderer's --font option.

Risk: Posting can publish content to selected social accounts.

Mitigation: Review the exact slides, caption, accounts, and settings, then require explicit confirmation before posting.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/social-media-skills/skills/tiktok-slideshow-skill)
- [SLIDE framework](references/slide-framework.md)
- [Slideshow recipes](references/slideshow-recipes.md)
- [Multi-account testing](references/multi-account-testing.md)
- [TikTok photo slideshow guidance](references/slideshow-2026-reality.md)
- [WoopSocial posting guide](references/woopsocial.md)
- [WoopSocial MCP tools reference](https://docs.woopsocial.com/mcp/tools-reference)
- [TikTok Sans](https://github.com/tiktok/TikTokSans)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Image files, Guidance]

**Output Format:** [Markdown plans and captions, JSON slide specifications, and rendered JPEG slides]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [TikTok 9:16 slides and Instagram 4:5 copies; publishing requires user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
