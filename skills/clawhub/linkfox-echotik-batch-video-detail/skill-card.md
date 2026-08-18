## Description:

EchoTik-视频详情 batch-fetches TikTok video detail, engagement, creator, and commerce metrics for known video IDs or URLs so sellers and marketers can compare video performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agents use this skill to retrieve and compare performance metrics for TikTok videos when they already have specific video IDs or TikTok video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox receives submitted TikTok video IDs or URLs and returns analytics estimates.

Mitigation: Install and use the skill only when sharing those IDs or URLs with LinkFox is acceptable, and avoid submitting sensitive or private identifiers.

Risk: The skill handles LinkFox API keys and can guide account login, SMS-code onboarding, and billing flows.

Mitigation: Provide phone numbers, SMS codes, API keys, and payment choices only when intentionally onboarding or purchasing credits.

Risk: Environment overrides can change the LinkFox API hosts used by the scripts.

Mitigation: Avoid LinkFox host override environment variables unless the replacement endpoint has been reviewed and trusted.

Risk: Full API responses and payment QR images may be retained in local LinkFox session directories.

Mitigation: Review saved file paths and remove local outputs that should not be retained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-batch-video-detail)
- [EchoTik batch video detail API reference](references/api.md)
- [Authentication and billing onboarding guide](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown summaries and comparison tables with saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under a LinkFox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
