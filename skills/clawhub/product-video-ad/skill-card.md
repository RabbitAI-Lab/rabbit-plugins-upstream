## Description:

Helps create short product ads from selling points by planning shots, generating video clips, assembling them, and adding subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to turn product benefits into a shot-by-shot script and a short advertising video with captions for distribution on social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ad prompts and selected product or model reference images may be sent to a cloud generation provider.

Mitigation: Confirm the selected provider and its data handling before use; share only images and prompts approved for external processing.

Risk: Generation may incur charges or use a provider different from the one expected.

Mitigation: Select the provider explicitly, preview the shot plan with --dry-run, and use scoped, revocable API keys.

Risk: The example brand profile includes demographic defaults that may not fit the intended campaign.

Mitigation: Replace the example model and brand settings with campaign-appropriate choices and review the ad for compliance before publication.

## Reference(s):

- [Product Video Ad release](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backend configuration](artifact/references/video-backends.md)
- [Provider setup and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and a JSON shot list with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the workflow can produce MP4 clips, a combined video, and SRT captions; voiceover and music require separate editing.]

## Skill Version(s):

1.0.14 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
