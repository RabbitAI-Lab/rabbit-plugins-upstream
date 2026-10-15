## Description:

Creates short product ads from selling points by drafting storyboards, generating individual shots, and assembling captioned video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creators use this skill to turn product selling points and reference images into storyboarded, captioned short-form ads for promotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images are sent to the selected external generation provider.

Mitigation: Choose a trusted provider and do not submit private or unreleased assets unless your data policy permits it.

Risk: Untrusted image URLs or files may be used as generation inputs.

Mitigation: Supply only trusted image URLs or local files, and review the storyboard and dry-run before generating.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider setup and data flow](artifact/references/provider-cli.md)
- [Video backends and captioning](artifact/references/video-backends.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Storyboard text, JSON shot plan, and commands for video generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the workflow can produce MP4 shots and a finished ad, plus SRT captions; it does not add voiceover or music.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
