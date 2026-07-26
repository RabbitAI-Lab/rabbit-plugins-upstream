## Description: <br>
Generate images and videos via Runware API, including text-to-image, image-to-image, upscaling, text-to-video, and image-to-video workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[26medias](https://clawhub.ai/user/26medias) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creative operators use this skill to generate, transform, upscale, and animate media through Runware models from agent-driven CLI workflows. It is useful when an agent needs to prepare Runware commands, choose generation parameters, or save generated images and videos locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and selected source images are sent to Runware for generation or transformation. <br>
Mitigation: Avoid sensitive or regulated media unless Runware's terms and data handling meet the user's requirements. <br>
Risk: Generated requests may consume paid Runware credits, and passing an API key on the command line can expose it in shell history or process listings. <br>
Mitigation: Prefer the RUNWARE_API_KEY environment variable over --api-key and review generation parameters before running commands. <br>


## Reference(s): <br>
- [Runware](https://runware.ai) <br>
- [Runware Models](https://runware.ai/models) <br>
- [Runware Pricing](https://runware.ai/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; generated image or video files are saved locally by the scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Runware API key and may use paid Runware credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
