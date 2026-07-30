## Description: <br>
Creates product launch and promo videos from a product URL, pasted script, or brief, including SaaS promos, feature reveals, product demos, app launches, and site tours. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and marketing teams use this skill to turn a product site, launch brief, or script into a HyperFrames product launch video with captured assets, storyboarded scenes, narration or music, animated HTML frames, and a final MP4 render. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can silently update globally installed HyperFrames skills before use. <br>
Mitigation: Review the update step before installation and disable it or require confirmation if silent global updates are not acceptable. <br>
Risk: The workflow performs network and media actions, including crawling target websites and using configured credentials or API keys for narration and music. <br>
Mitigation: Verify the target URL before capture and provide only credentials or API keys that are intended for this workflow. <br>
Risk: Previously recorded project preferences may influence a new video workflow. <br>
Mitigation: Reset old project preferences or review BRIEF.md before generation when prior context should not be reused. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/product-launch-video) <br>
- [Story design](references/story-design.md) <br>
- [Visual design](references/visual-design.md) <br>
- [Motion language](references/motion-language.md) <br>
- [Cut catalog](references/cut-catalog.md) <br>
- [Frame worker delta](sub-agents/frame-worker.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown workflow guidance with inline shell commands and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces HyperFrames project assets such as BRIEF.md, STORYBOARD.md, SCRIPT.md, HTML frame compositions, captions, audio metadata, an assembled index, snapshots, and renders/video.mp4 when the workflow completes.] <br>

## Skill Version(s): <br>
1.0.22 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
