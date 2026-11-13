## Description:

Build a moodboard that AI image and video models can follow, then check test stills against it before generating video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Video creators, artists, and developers use the skill to turn a brief and visual references into a specific style guide for AI image and video generation. It produces a visual board and checks sample stills against details such as palette, lighting, and framing before video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands use unpinned versions, so the installed content may change over time.

Mitigation: Review the install command and pin a trusted version or commit before running it.

Risk: The workflow may send prompts or images to external image services with different privacy practices.

Mitigation: Check each provider's privacy terms and avoid sending confidential prompts or images.

## Reference(s):

- [Moodboard research and evidence](https://varg.ai/how-to/make-a-moodboard-for-an-ai-video)
- [Dimension writing guide](artifact/references/dimensions.md)
- [Moodboard template](artifact/references/moodboard-template.md)
- [Reference links](artifact/references/links.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Image files, Analysis, Guidance]

**Output Format:** [Markdown moodboard and checks, an HTML visual board, and optional test still images.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a creative brief and visual references; palette extraction and checks require Python 3 and Pillow. Test still generation may use external image services.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
