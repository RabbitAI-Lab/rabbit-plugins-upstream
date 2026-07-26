## Description: <br>
Add word-timed captions to an Open Recut program by mapping a canonical transcript through timeline.json, reviewing a maintained caption style on source-backed pixels, rendering a local transparent HyperFrames PNG sequence, and registering it as an overlay contribution for the shared delivery render. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video-production agents use this skill to add reviewed, word-timed caption overlays to an existing Open Recut project after video understanding has produced a validated transcript and timeline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow runs local media tooling, Node scripts, npx hyperframes, and opens local review HTML. <br>
Mitigation: Review the skill before installation, run it in a controlled local workspace, and confirm the required media tools and browser runtime behavior are acceptable. <br>
Risk: Referenced runtime assets may be missing from the packaged artifact. <br>
Mitigation: Verify fonts, preview assets, and runtime files are present before processing media; stop and repair the package if required assets are unavailable. <br>
Risk: Caption approval depends on source-backed review evidence and exact human or delegated agent decisions. <br>
Mitigation: Require the style review, preview review, and hash-bound interaction receipt before rendering or registering the caption overlay. <br>


## Reference(s): <br>
- [Video Add Captions on ClawHub](https://clawhub.ai/whitetowerai/skills/video-add-captions) <br>
- [Caption Rules and Data Shape](reference/caption-rules.md) <br>
- [Caption Style Themes](reference/caption-style-themes.md) <br>
- [Caption Feedback Mapping](reference/caption-feedback-mapping.md) <br>
- [GSAP](https://gsap.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces caption plans, SRT files, review HTML, evidence images, transparent PNG overlay frames, and project registration updates.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
