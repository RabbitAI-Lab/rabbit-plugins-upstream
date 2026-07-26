## Description: <br>
Make video that looks shot, not generated, with deliberate framing, lens, camera motion, lighting, and color grade. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to turn text briefs or source stills into cinematic short-video prompts and Runware videoInference request guidance for text-to-video or image-to-video workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image-to-video workflows can send user-provided source images to an external provider. <br>
Mitigation: Confirm the user is comfortable sharing the source image with the provider before submitting a job. <br>
Risk: Generated clips are returned through external video URLs. <br>
Mitigation: Review sharing, retention, and access expectations before using or distributing returned video links. <br>
Risk: Video model schemas, dimensions, duration values, costs, and content constraints may change. <br>
Mitigation: Confirm the live model schema and provider constraints before running videoInference requests. <br>


## Reference(s): <br>
- [Cinematic video: worked recipes](references/examples.md) <br>
- [Cinematic Video on ClawHub](https://clawhub.ai/runware/skills/cinematic-video) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with JSON videoInference request examples and videoURL result shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides asynchronous video generation and polling; image-to-video workflows may send source images to the provider.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
