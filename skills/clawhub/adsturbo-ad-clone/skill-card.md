## Description:

Analyzes a reference ad into shots and prompts, then helps create a new video with a similar structure or inspect the ad without generating video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Advertisers and creators use this skill to break down a reference ad, adapt its shots or dialogue, and generate a new video; they can also request analysis without generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A draft submission can spend AdsTurbo credits without a built-in confirmation check.

Mitigation: Show the previewed credit quote and obtain explicit user confirmation before submitting a draft or starting generation.

Risk: Source media must be publicly accessible and uploads can expose private or unauthorized material.

Mitigation: Upload only material the user is authorized to share, and avoid private media.

Risk: The AdsTurbo API key grants access to billable operations.

Mitigation: Keep the key in an environment variable and never include it in replies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/adsturbo/skills/adsturbo-ad-clone)
- [Ad Clone guide](references/ad_clone.md)
- [Upload guide](references/upload.md)
- [Work Status guide](references/work.md)
- [AdsTurbo API key](https://adsturbo.ai/iris/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with shot breakdowns, prompts, and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation is asynchronous; analysis-only use does not generate a video.]

## Skill Version(s):

1.2.3 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
