## Description: <br>
Turns arbitrary text into a faceless explainer video with invented visuals such as typography, abstract graphics, diagrams, and data visualization for topic explainers, concept breakdowns, how-tos, and listicles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, video producers, and agent operators use this skill to turn text, notes, topics, or briefs into HyperFrames explainer videos with storyboard, narration, invented visuals, HTML frame compositions, captions, and a final MP4. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill tells the agent to silently update global HyperFrames skills from the network during normal use. <br>
Mitigation: Require explicit approval before running update commands, and review the updated global skill set before continuing with video generation. <br>
Risk: Generated HTML or caption output may rely on CDN dependencies, which can matter in offline or locked-down rendering environments. <br>
Mitigation: Review generated HTML and CDN references before deployment, and replace or approve dependencies according to the target environment's policy. <br>


## Reference(s): <br>
- [Faceless Explainer ClawHub page](https://clawhub.ai/heygen-com/skills/faceless-explainer) <br>
- [Story design](artifact/references/story-design.md) <br>
- [Visual design](artifact/references/visual-design.md) <br>
- [Motion language](artifact/references/motion-language.md) <br>
- [Cut catalog](artifact/references/cut-catalog.md) <br>
- [Frame worker delta](artifact/sub-agents/frame-worker.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown project files, JSON metadata, shell commands, HTML frame compositions, captions, and rendered MP4 artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates project-local video assets under videos/<project>; audio and media behavior depends on HyperFrames, HeyGen sign-in status, and available local fallbacks.] <br>

## Skill Version(s): <br>
1.0.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
