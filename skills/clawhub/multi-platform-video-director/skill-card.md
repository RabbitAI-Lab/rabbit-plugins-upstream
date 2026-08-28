## Description:

Turns reference images or text descriptions into executable video plans, platform-adapted prompts, storyboard and motion guidance, and generated or edited video assets when compatible tools are available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yeshenyue12345](https://clawhub.ai/user/yeshenyue12345)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to convert image or text ideas into short-form video generation prompts, platform routing decisions, storyboards, subtitles, background music, voice lines, and local media assembly commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video generation can consume credits and may send prompts, images, or other user-provided media to connected generation services.

Mitigation: Confirm credit-consuming generation and avoid submitting sensitive media or text unless the user accepts that service exposure.

Risk: Online text-to-speech may transmit user-provided dialogue to a TTS service.

Mitigation: Use TTS only when requested and avoid sending sensitive dialogue unless external processing is acceptable.

Risk: Generated or edited videos can misrepresent people, brands, legal text, medical content, news imagery, or other identity-sensitive material.

Mitigation: Preserve protected anchors such as faces, logos, and precise text, avoid prohibited transformations, and review outputs before use.

Risk: Local media scripts process user-supplied files and optional Python dependencies.

Mitigation: Run scripts in a managed workspace environment, verify input paths, and install only the declared dependencies needed for the requested media operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yeshenyue12345/skills/multi-platform-video-director)
- [Platform Routing and Syntax Guide](references/platform-routing.md)
- [Image-to-Video Prompt Pattern Library](references/prompt-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code]

**Output Format:** [Markdown with prompts, parameter blocks, JSON-like tool calls, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify local video, audio, subtitle, and metadata files when compatible media tools and dependencies are available.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
