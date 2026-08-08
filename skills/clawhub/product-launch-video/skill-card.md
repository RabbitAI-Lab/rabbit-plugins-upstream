## Description:

Turns a product URL, pasted script, or brief into a HyperFrames product launch or promo video with captured assets, storyboard and script planning, frame builds, audio, captions, transitions, and final render steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to turn a commercial product URL, launch brief, or promotional script into a structured HyperFrames project and final promo video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may silently update installed skills before use.

Mitigation: Disable or manually approve the update step before running the skill in controlled environments.

Risk: The workflow captures commercial URLs and may use external services during audio or media steps.

Mitigation: Run it only on product URLs intended for video creation, and review sign-in and provider status before audio generation.

Risk: Autonomous execution can be unsuitable for sensitive or ambiguous product sites.

Mitigation: Use collaborative review gates for sensitive inputs and avoid autonomous mode when the source or intended message is unclear.

## Reference(s):

- [Product Launch Video ClawHub Page](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [story-design.md](references/story-design.md)
- [visual-design.md](references/visual-design.md)
- [motion-language.md](references/motion-language.md)
- [cut-catalog.md](references/cut-catalog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown instructions with shell commands and generated project files, including storyboard/script markdown, HTML frame code, JSON timing metadata, captions, and an MP4 render.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a HyperFrames project under videos/<project>/ and uses review gates before final rendering.]

## Skill Version(s):

1.0.25 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
