## Description: <br>
Guides an agent to use the RunComfy CLI for video outpainting, aspect-ratio conversion, and spatial canvas extension while preserving central action. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creative operators, and agent users use this skill to route video outpainting requests through RunComfy, choose between the Wan 2-7 Edit-Video CLI path and ComfyUI workflows, and prepare safe commands for expanding a video's spatial frame. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source video URLs, prompts, and output files are sent to RunComfy for remote processing. <br>
Mitigation: Confirm user consent before submitting media or prompts, use the documented RunComfy endpoints, and review generated outputs before publishing or reusing them. <br>
Risk: The skill depends on local RunComfy authentication through a stored token or RUNCOMFY_TOKEN. <br>
Mitigation: Store tokens using the documented RunComfy login flow or environment variable, avoid exposing credentials in logs, and rotate tokens if they are shared accidentally. <br>
Risk: Outpainting quality may vary, especially around seams or after repeated passes. <br>
Mitigation: Use the Wan 2-7 Edit-Video path for quick aspect changes and switch to dedicated ComfyUI outpainting workflows when strict temporal consistency or hero-quality seams are required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/video-outpainting) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [Wan 2-7 edit-video](https://www.runcomfy.com/models/wan-ai/wan-2-7/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=video-outpainting) <br>
- [RunComfy CLI docs](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=video-outpainting) <br>
- [LTX 2-3 outpainting in ComfyUI](https://www.runcomfy.com/comfyui-workflows/ltx-2-3-outpainting-in-comfyui-spatial-frame-expansion-workflow?utm_source=clawhub&utm_medium=skill&utm_campaign=video-outpainting) <br>
- [RunComfy CLI troubleshooting](https://docs.runcomfy.com/cli/troubleshooting?utm_source=clawhub&utm_medium=skill&utm_campaign=video-outpainting) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with bash and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may require the runcomfy CLI, RunComfy authentication, outbound network access, and an output directory for generated video files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
