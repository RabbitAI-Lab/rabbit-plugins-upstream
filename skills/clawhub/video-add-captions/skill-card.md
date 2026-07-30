## Description: <br>
Add word-timed captions to an Open Recut program by mapping the canonical transcript through timeline.json, reviewing a maintained caption style on source-backed pixels, rendering a local transparent HyperFrames PNG sequence, and registering it as an overlay contribution for shared delivery render. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video-production agents use this skill to add reviewed, word-timed captions to an existing Open Recut project after transcript and timeline analysis are complete. It supports caption grouping, style review, transparent overlay rendering, and project registration without changing cuts, source timing, grading, reframing, or audio policy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package appears incomplete because a font file required by the generator and self-check is missing. <br>
Mitigation: Confirm required runtime assets are present and run the caption self-checks before installing or using the skill on production projects. <br>
Risk: The workflow runs local render tools, may fetch HyperFrames through npx, and opens local review pages. <br>
Mitigation: Review commands before execution, use a controlled local environment, and allow network package fetches only when they match the intended workflow. <br>
Risk: Generated cache metadata can store local absolute paths. <br>
Mitigation: Review generated metadata and avoid sharing cache artifacts or logs that expose local filesystem paths. <br>


## Reference(s): <br>
- [Caption Rules and Data Shape](reference/caption-rules.md) <br>
- [Caption Style Themes](reference/caption-style-themes.md) <br>
- [Caption Feedback Mapping](reference/caption-feedback-mapping.md) <br>
- [GSAP](https://gsap.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/whitetowerai/skills/video-add-captions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated JSON, SRT, HTML review pages, PNG overlay frames, and project configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces durable caption plans, review evidence, subtitles, transparent PNG overlay frames, and project registration updates in the local video project.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
