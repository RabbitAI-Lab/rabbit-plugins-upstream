## Description: <br>
Turn a still image into a short video by directing subject, camera, and atmospheric motion, including optional motion transfer from a reference video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to have an agent collect a source still, motion brief, and optional reference video, then submit asynchronous image-to-video generation jobs through Runware models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may submit selected images, videos, and prompts to external video-generation services. <br>
Mitigation: Use only media and prompts that are acceptable to send to the selected provider, and avoid sensitive personal or confidential content unless that provider use is approved. <br>
Risk: Model schemas and allowed parameters can change over time. <br>
Mitigation: Resolve the live model schema before each run and avoid hardcoding model AIRs, input fields, duration, or dimension values. <br>
Risk: Unsupported motion can produce warped or misleading video output. <br>
Mitigation: Keep motion grounded in visible source-image evidence, state which channels should hold still, and retry with a better-matched still or reference video when the result drifts. <br>


## Reference(s): <br>
- [Animate image worked recipes](artifact/references/examples.md) <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/animate-image) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, JSON, Video links] <br>
**Output Format:** [Markdown guidance with JSON request examples and final video URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs video generation asynchronously; final clips are returned as MP4 or sequence links when the provider job completes.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
