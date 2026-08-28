## Description:

Create polished Chinese story short videos from story text or ordered illustrations with story-specific hand-drawn scenes, a text-led opening poster, sentence-synchronous local Qwen3-TTS narration, subtitles, and licensed background music mixed beneath narration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT

## Use Case:

Creators, educators, and developers use this skill to produce Chinese idiom, children's story, and history explainer shorts with distinct illustrated scenes, synchronized narration, captions, and final MP4 delivery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Python ML dependencies and local model downloads can introduce dependency or supply-chain risk.

Mitigation: Install in a project-controlled virtual environment, use trusted Qwen model IDs or model paths, and keep torch and related packages on patched current versions.

Risk: Background music may have license or attribution obligations.

Mitigation: Use only BGM whose license permits the intended use and retain source, author, and license attribution beside the final deliverable.

Risk: Intermediate silent picture tracks or mismatched narration can be mistaken for a finished narrated video.

Mitigation: Verify poster ratio, scene timing, subtitle and narration alignment, and final H.264/AAC audio mix before exposing the MP4 as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tobewin/skills/narrated-handdrawn-story-video)
- [Server-resolved GitHub provenance](https://github.com/ToBeWin/narrated-handdrawn-story-video)
- [Bundled upstream renderer](https://github.com/gnipbao/story-to-handdrawn-video)
- [Remotion](https://www.remotion.dev/)
- [Ma Shan Zheng font](https://github.com/googlefonts/mashanzheng)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands, JSON storyboard guidance, and production checklist text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to produce storyboard assets, narration audio, attribution text, and a final H.264/AAC MP4; intermediate media should not be treated as final deliverables.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
