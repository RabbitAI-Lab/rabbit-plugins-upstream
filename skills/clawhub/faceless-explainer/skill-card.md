## Description: <br>
Turns arbitrary text, such as an article, notes, topic, or brief, into a faceless explainer video with invented scene visuals such as typography, abstract graphics, diagrams, and data visualizations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video-creation agents use this skill to transform source text into a HyperFrames explainer workflow, including the brief, storyboard, script, visual direction, frame compositions, captions, audio metadata, preview, and final video render. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs the agent to silently self-update and globally update related HyperFrames skills from GitHub. <br>
Mitigation: Review the skill before installation, remove or ignore the silent self-update instruction, run updates manually, and prefer locally bundled animation assets when reproducibility matters. <br>


## Reference(s): <br>
- [Story design](references/story-design.md) <br>
- [Visual design](references/visual-design.md) <br>
- [Motion language](references/motion-language.md) <br>
- [Cut catalog](references/cut-catalog.md) <br>
- [Frame worker delta](sub-agents/frame-worker.md) <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration and metadata, HTML frame code, caption data, and MP4 render output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces project files under a HyperFrames video workspace, including storyboard, script, frame compositions, index, captions, audio metadata, snapshots, and a final MP4 when approved.] <br>

## Skill Version(s): <br>
1.0.19 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
