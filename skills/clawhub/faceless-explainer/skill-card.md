## Description:

Turns text into faceless explainer videos with invented visuals, such as animated typography, diagrams, and data visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and video teams use this skill to turn articles, notes, topics, or briefs into faceless explainer videos with custom animated visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HyperFrames commands can fetch mutable tooling and update installed skills globally.

Mitigation: Review or pin the HyperFrames CLI and approve updates before running the workflow.

Risk: The workflow can contact external services and use existing HeyGen credentials for media and rendering.

Mitigation: Confirm service access and credential scope before submitting source material or starting renders.

Risk: The workflow writes video project files and rendered media.

Mitigation: Run it in an intended project directory and review generated artifacts before sharing.

## Reference(s):

- [Story design](artifact/references/story-design.md)
- [Visual design](artifact/references/visual-design.md)
- [Motion language](artifact/references/motion-language.md)
- [Cut catalog](artifact/references/cut-catalog.md)

## Skill Output:

**Output Type(s):** [Video, Markdown, Code, Configuration]

**Output Format:** [MP4 video with supporting Markdown, HTML, and JSON project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Narration, music, and captions depend on the project brief and available services.]

## Skill Version(s):

1.0.39 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
