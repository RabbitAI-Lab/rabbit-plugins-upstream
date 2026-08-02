## Description: <br>
Turns a music track into a beat-synced HyperFrames video, using the music to drive timing, storyboard planning, frame composition, assembly, verification, and MP4 rendering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to turn an audio file, video-derived audio track, or generated mood track into a beat-synced lyric video, slideshow, or kinetic promo. It guides an agent through setup, audio analysis, storyboard planning, per-frame composition, assembly, review, and rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that the skill can update global HyperFrames skills from the network before use. <br>
Mitigation: Install and run it only in an isolated project and Python environment, and require confirmation before updates or package installs. <br>
Risk: The security scan reports unmanaged flashing effects and possible third-party resource loading in generated videos. <br>
Mitigation: Review rendered videos for flash and flicker safety, and inspect third-party resource loading before publishing. <br>


## Reference(s): <br>
- [Frame Skeleton](references/frame-skeleton.md) <br>
- [Planning](references/planning.md) <br>
- [Storyboard Format](references/storyboard-format.md) <br>
- [Template Catalog](references/template-catalog.md) <br>
- [Motion Primitive Catalog](references/motion-primitive-catalog.md) <br>
- [Asset Treatments](references/montage.md) <br>
- [Frame Worker](sub-agents/frame-worker.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/music-to-video) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated project files such as JSON audio analysis, Markdown storyboards, HTML compositions, and MP4 renders.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a staged HyperFrames project and uses approval gates for plan review and render review.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
