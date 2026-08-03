## Description: <br>
Pose-conditioned generation on RunComfy via the runcomfy CLI, routing image and video requests across Kling Motion Control, Wan 2-2 Animate, and Z-Image Turbo ControlNet LoRA based on the requested control type and output mode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and creative automation users can use this skill to ask an agent for pose-, motion-, depth-, or edge-conditioned image and video generation through RunComfy. The skill helps choose an appropriate RunComfy model route and produce the CLI command shape needed to submit the job. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and media URLs are sent to RunComfy as an external cloud service. <br>
Mitigation: Install only when the user is comfortable with that service boundary and avoid sending private prompts or assets unless approved for RunComfy use. <br>
Risk: The RunComfy token may grant access to the user's RunComfy account. <br>
Mitigation: Keep the token scoped and removable, and prefer RUNCOMFY_TOKEN or ~/.config/runcomfy storage that can be rotated or deleted. <br>
Risk: Reference videos, character images, and control images can be untrusted inputs. <br>
Mitigation: Use only assets intentionally provided by the user and check unexpected output divergence against the supplied reference assets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/controlnet-pose) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=controlnet-pose) <br>
- [Kling 2-6 Motion Control Pro](https://www.runcomfy.com/models/kling/kling-2-6/motion-control-pro?utm_source=clawhub&utm_medium=skill&utm_campaign=controlnet-pose) <br>
- [Kling 2-6 Motion Control Standard](https://www.runcomfy.com/models/kling/kling-2-6/motion-control-standard?utm_source=clawhub&utm_medium=skill&utm_campaign=controlnet-pose) <br>
- [Wan 2-2 Animate video-to-video](https://www.runcomfy.com/models/community/wan-2-2-animate/video-to-video?utm_source=clawhub&utm_medium=skill&utm_campaign=controlnet-pose) <br>
- [Z-Image Turbo ControlNet LoRA](https://www.runcomfy.com/models/tongyi-mai/z-image/turbo/controlnet/lora?utm_source=clawhub&utm_medium=skill&utm_campaign=controlnet-pose) <br>
- [RunComfy Kling collection](https://www.runcomfy.com/models/collections/kling?utm_source=clawhub&utm_medium=skill&utm_campaign=controlnet-pose) <br>
- [Mastering ControlNet tutorial](https://www.runcomfy.com/tutorials/mastering-controlnet-in-comfyui?utm_source=clawhub&utm_medium=skill&utm_campaign=controlnet-pose) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the runcomfy CLI plus RUNCOMFY_TOKEN or ~/.config/runcomfy authentication; generated media is downloaded by the CLI to the requested output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
