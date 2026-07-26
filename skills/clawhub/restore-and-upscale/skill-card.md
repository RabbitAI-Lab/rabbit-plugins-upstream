## Description: <br>
Improves image quality and resolution by routing degraded or low-resolution images to appropriate restoration, deblurring, denoising, dehazing, artifact removal, and upscaling workflows without changing the underlying content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to choose and run the right image or video restoration workflow for blurry, noisy, hazy, damaged, compressed, or low-resolution media while preserving the original subject where fidelity matters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Supplied images or videos may be sent to external model workflows for restoration or upscaling. <br>
Mitigation: Confirm the user intends to use those external workflows and avoid submitting sensitive media unless the deployment policy allows it. <br>
Risk: Vague requests such as "enhance" can be routed to an unwanted restoration, beautification, or video workflow. <br>
Mitigation: Clarify whether the user wants faithful cleanup, creative detail enhancement, broader editing, or a dedicated video-upscale path before running a model. <br>
Risk: Diffusion-based restoration can introduce plausible but invented detail, especially for documents, faces, and identity-sensitive images. <br>
Mitigation: Prefer faithful non-diffusion paths when accuracy matters, inspect outputs at full resolution, and state the no dedicated face-restoration limitation plainly. <br>


## Reference(s): <br>
- [Restore and upscale - worked recipes](artifact/references/examples.md) <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/restore-and-upscale) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Configuration] <br>
**Output Format:** [Markdown with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model routing choices, schema checks, request payloads, and image or video result URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
