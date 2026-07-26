## Description: <br>
Turn a music track, source video audio, or mood-generated track into a beat-synced lyric video, slideshow, or kinetic promo where music drives pacing and optional user media is cut to the same beat grid. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative agents use this skill to plan and build music-grounded HyperFrames videos from a provided or generated track, optional images or videos, and beat analysis. It supports storyboard planning, frame composition, assembly, verification, and final MP4 rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs agents to silently update global HyperFrames skills before use. <br>
Mitigation: Require explicit user confirmation before running any global skill update or other package-changing npx command. <br>
Risk: The workflow can install Python dependencies, use authenticated media providers, and run render steps. <br>
Mitigation: Confirm dependency installation, authenticated provider use, and rendering actions before execution, and keep credentials out of project-local environment files. <br>
Risk: Some bundled visual templates use strobe-like effects that may be unsuitable for photosensitive audiences. <br>
Mitigation: Avoid strobe templates or substitute lower-flash motion treatments when the audience may include photosensitive viewers. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/music-to-video) <br>
- [Frame Skeleton](references/frame-skeleton.md) <br>
- [Planning](references/planning.md) <br>
- [Storyboard Format](references/storyboard-format.md) <br>
- [Template Catalog](references/template-catalog.md) <br>
- [Motion Primitive Catalog](references/motion-primitive-catalog.md) <br>
- [Montage](references/montage.md) <br>
- [Frame Worker](sub-agents/frame-worker.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown storyboards, JSON timing data, HTML/CSS/JavaScript frame files, shell commands, configuration files, and rendered video artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project files under a video workspace and a final MP4 render after verification and approval.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
