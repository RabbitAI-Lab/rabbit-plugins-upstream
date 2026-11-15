## Description:

Build, deploy and verify static landing pages for ChatGPT / OpenAI Ads campaigns — any advertiser, any vertical — using the chatgpt-ads-landing engine (pages/<slug>/ + page.json → build → check → zip) and an optional compatible site-hosting platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xt-felix](https://clawhub.ai/user/xt-felix)

### License/Terms of Use:

MIT

## Use Case:

Advertisers and developers use this skill to create and update campaign landing pages, configure market-specific destinations, privacy and measurement, and prepare pages for hosting. It also guides local and live checks of crawlability, routing, consent, and pixel events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consent behavior and public-access settings may create privacy or deployment safety issues.

Mitigation: Review the consent flow and public-access settings for each page before deployment.

Risk: The reported deployment and preview-server risks may affect how pages are exposed during setup or review.

Mitigation: Check hosting and preview-server access settings before using them with client pages.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xt-felix/skills/chatgpt-ads-landing)
- [OpenAI Ads policies](https://openai.com/policies/ad-policies/)
- [OpenAI crawler guidance](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers)
- [OpenAI Ads Measurement Pixel](https://developers.openai.com/ads/measurement-pixel)
- [OpenAI Ads Image Tag](https://developers.openai.com/ads/image-tag)
- [OpenAI Ads supported events](https://developers.openai.com/ads/supported-events)
- [page-config.md](artifact/references/page-config.md)
- [pixel-events.md](artifact/references/pixel-events.md)
- [privacy-consent.md](artifact/references/privacy-consent.md)
- [platform-deploy.md](artifact/references/platform-deploy.md)

## Skill Output:

**Output Type(s):** [Code, Files, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Static HTML, CSS and JavaScript pages; JSON configuration; shell commands; Markdown guidance and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Campaign content, destinations, tracking events and market settings are supplied per client.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
