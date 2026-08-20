## Description:

Turns arbitrary text such as articles, notes, topics, or briefs into faceless explainer videos with invented typography, abstract graphics, diagrams, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to convert supplied text into a HyperFrames explainer project with a storyboard, script, audio metadata, animated HTML frame compositions, previews, and a rendered MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic skill updates may change installed workflow behavior before execution.

Mitigation: Review update policy before installation or execution, and scan the resolved skill contents before use.

Risk: Generated video HTML can load third-party CDN scripts.

Mitigation: Review allowed external script sources and render in an environment where outbound access is approved.

Risk: User-provided source text may be saved in project files or sent to configured audio and media providers.

Mitigation: Avoid sensitive inputs unless project storage and provider routing are approved; use offline or silent modes when appropriate.

## Reference(s):

- [Story design - faceless explainer video](references/story-design.md)
- [Visual design - faceless-explainer per-frame shot method](references/visual-design.md)
- [Motion language - the move vocabulary, motion doctrine, and seek-safe core](references/motion-language.md)
- [Cut catalog - within-frame seams](references/cut-catalog.md)
- [Faceless Explainer on ClawHub](https://clawhub.ai/heygen-com/skills/faceless-explainer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON project files, HTML/CSS/JavaScript frame compositions, shell commands, and MP4 render output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates project-local video files under videos/<project>/ and may use configured audio or media providers.]

## Skill Version(s):

1.0.23 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
