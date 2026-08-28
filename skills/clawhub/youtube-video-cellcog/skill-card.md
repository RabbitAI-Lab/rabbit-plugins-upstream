## Description:

AI YouTube content creation powered by CellCog for videos, Shorts, thumbnails, scripts, tutorials, vlogs, educational videos, product reviews, and video essays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, educators, and developers use this skill to plan and request YouTube videos, Shorts, thumbnails, scripts, outlines, and related content through CellCog. It is intended for normal ClawHub use where the operator supplies a CellCog API key and reviews generated media before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a CellCog API key and sends video-generation work to an external CellCog service.

Mitigation: Use a dedicated CellCog key, follow CellCog setup guidance, and avoid submitting sensitive material unless the operator has approved that service use.

Risk: Generated video or thumbnail work can consume credits and may not produce a usable result.

Mitigation: Review CellCog pricing and run small tests before large video-generation tasks.

Risk: Generated media may be unsuitable for publication without human review.

Mitigation: Review scripts, thumbnails, videos, and claims before publishing to YouTube.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cellcog/skills/youtube-video-cellcog)
- [CellCog](https://cellcog.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python snippets, setup commands, and task prompts; CellCog may return generated media or messages from the external service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; results and cost depend on CellCog service behavior and requested media complexity.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
