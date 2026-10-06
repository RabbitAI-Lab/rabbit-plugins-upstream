## Description:

Creates local-first visual artifacts from user-provided text, articles, and data, including infographics, reports, data posters, browser decks, and optional explanatory media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaoshou.dev](https://clawhub.ai/user/miaoshou.dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users invoke the skill to turn their own articles, text, and local datasets into shareable visual reports, infographics, posters, or presentations. They can also validate report or deck specifications and optionally generate an image or video from a verified conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the shared CLI downloads a binary and persists it locally.

Mitigation: Prefer packaged installation; require separate approval before installing the pinned CLI and its checksum.

Risk: Optional paid media generation sends the chosen prompt and reference materials to remote model providers.

Mitigation: Show the exact upload scope and expected charges, and obtain user approval before generation.

## Reference(s):

- [Miao Vision on ClawHub](https://clawhub.ai/miaoshou.dev/skills/miao-vision-skill)
- [Report workflow](references/report.md)
- [Article infographic workflow](references/article.md)
- [Browser deck workflow](references/deck.md)
- [Optional AI media setup](references/media-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with artifact links and optional setup or validation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent delivers links to generated local HTML/PDF, image, or video artifacts and previews when available.]

## Skill Version(s):

0.10.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
