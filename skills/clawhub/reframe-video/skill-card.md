## Description: <br>
Convert a video to a new aspect ratio without cropping the subject by using model outpainting to extend the scene edges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and developers use this skill to adapt finished clips for vertical, square, or other target canvases while preserving the subject. It guides agents through schema confirmation, video inference, prompting, source positioning, and quality review for reframed outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill can upload source video to an external model provider. <br>
Mitigation: Confirm the user has rights to process the source video and approval to use the target provider before running the job. <br>
Risk: Video reframing jobs can incur per-second generation costs and depend on currently supported model schemas and resolutions. <br>
Mitigation: Check pricing, live model status, supported width and height pairs, and the schema before submitting inference. <br>
Risk: Outpainted edges may drift from the original scene or introduce unrelated generated content. <br>
Mitigation: Review the output video and retry with a clearer surroundings prompt or adjusted source position when the extension does not match the source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/reframe-video) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, API Calls] <br>
**Output Format:** [Markdown guidance with parameter names, workflow steps, and quality checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides asynchronous video inference and returns instructions for reading the generated video URL.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
