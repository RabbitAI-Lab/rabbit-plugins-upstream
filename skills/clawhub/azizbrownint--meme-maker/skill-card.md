## Description:

Search meme templates, suggest formats, and generate local or hosted image memes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search a curated meme-template registry, choose an appropriate format for a joke, and render a local SVG/PNG meme or request a hosted Imgflip render.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted rendering sends meme caption text to Imgflip.

Mitigation: Use the default local mode when captions should not be sent to a hosted service, and avoid putting sensitive text in meme captions.

Risk: Imgflip credentials may be exposed when supplied as command-line flags.

Mitigation: Prefer IMGFLIP_USER and IMGFLIP_PASS environment variables over username and password flags where process-list exposure matters.

Risk: The skill performs disclosed Imgflip network calls for hosted rendering, template-image downloads, and refresh operations.

Mitigation: Install only when Imgflip network access is acceptable, and use local rendering with the curated registry when hosted service use is not desired.

## Reference(s):

- [Curated template registry](references/templates.json)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/meme-maker)
- [Imgflip caption_image endpoint](https://api.imgflip.com/caption_image)
- [Imgflip get_memes endpoint](https://api.imgflip.com/get_memes)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON listings when requested, local SVG/PNG files, or a hosted Imgflip URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local mode caches downloaded template images; hosted mode sends captions to Imgflip and requires user-provided Imgflip credentials.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
