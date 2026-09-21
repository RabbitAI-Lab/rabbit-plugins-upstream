## Description:

Turn a research paper into a silent, general-audience explainer on a declarative HyperFrames video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runshengdu](https://clawhub.ai/user/runshengdu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, educators, and technical communicators use this skill to turn one research paper into an approved analysis, script, timeline, scene implementation, captions, and a silent 16:9 MP4 explainer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates local project files and media outputs.

Mitigation: Run it from a normal project directory and keep generated work contained under the paper-specific output directory.

Risk: The workflow uses FFmpeg and may install pinned npm packages into its runtime after setup approval.

Mitigation: Approve setup only when the required media tooling and isolated runtime are acceptable for the environment.

Risk: Generated explainers can contain errors or misleading visual summaries of the paper.

Mitigation: Review the analysis, storyboard, subtitles, rendered frames, and final MP4 before publishing.

## Reference(s):

- [Source repository](https://github.com/runshengdu/paper-to-video)
- [ClawHub skill page](https://clawhub.ai/runshengdu/skills/paper-to-video)
- [Paper analysis](artifact/references/paper-analysis.md)
- [Video script](artifact/references/video-script.md)
- [Clip timeline](artifact/references/clip-timeline.md)
- [HyperFrames workflow](artifact/references/hyperframes-workflow.md)
- [Visual grammar](artifact/references/visual-grammar.md)
- [Quality control](artifact/references/quality-control.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown analysis and script files, YAML timeline configuration, HTML/CSS/JavaScript scene files, SRT captions, review assets, and MP4 video output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces paper-specific outputs under output/<paper_short_name>/; final video is 1920x1080, 16:9, 30 fps, silent, and optionally contains burned-in subtitles.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
