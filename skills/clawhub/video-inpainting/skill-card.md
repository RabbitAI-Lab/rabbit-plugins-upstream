## Description: <br>
Region edits across video frames on RunComfy via the runcomfy CLI, including object removal, watermark cleanup, and region replacement with matching motion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to guide agents through region-based video edits with RunComfy, including choosing the best CLI-reachable model path for prompt-driven edits, identity-stable restyles, or frame-sequence workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source videos, prompts, and edit requests are sent to RunComfy's hosted service. <br>
Mitigation: Use the skill only for media intended for hosted processing, and avoid sending sensitive or unauthorized video content. <br>
Risk: The skill requires a RUNCOMFY_TOKEN for CLI access. <br>
Mitigation: Keep the token private, prefer environment or RunComfy config storage, and do not log or commit credentials. <br>
Risk: Untrusted source videos can influence model behavior or produce edits that diverge from the prompt. <br>
Mitigation: Use only user-provided source URLs for the requested edit and review outputs before relying on them. <br>
Risk: Video inpainting can remove watermarks, logos, people, or other content in ways that may violate rights or mislead viewers. <br>
Mitigation: Confirm authorization for the edit and review generated outputs for policy, rights, and disclosure requirements before public use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/permew/skills/video-inpainting) <br>
- [RunComfy](https://www.runcomfy.com) <br>
- [RunComfy CLI documentation](https://docs.runcomfy.com/cli/introduction?utm_source=clawhub&utm_medium=skill&utm_campaign=video-inpainting) <br>
- [Wan 2-7 edit-video model](https://www.runcomfy.com/models/wan-ai/wan-2-7/edit?utm_source=clawhub&utm_medium=skill&utm_campaign=video-inpainting) <br>
- [Seedream 4-0 edit-sequential model](https://www.runcomfy.com/models/bytedance/seedream-4-0/edit-sequential?utm_source=clawhub&utm_medium=skill&utm_campaign=video-inpainting) <br>
- [RunComfy ComfyUI workflows](https://www.runcomfy.com/comfyui-workflows?utm_source=clawhub&utm_medium=skill&utm_campaign=video-inpainting) <br>
- [LTX 2-3 targeted video inpaint workflow](https://www.runcomfy.com/comfyui-workflows/ltx-2-3-inpaint-in-comfyui-targeted-video-frame-editing?utm_source=clawhub&utm_medium=skill&utm_campaign=video-inpainting) <br>
- [Wan models collection](https://www.runcomfy.com/models/collections/wan-models?utm_source=clawhub&utm_medium=skill&utm_campaign=video-inpainting) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the runcomfy CLI, a RUNCOMFY_TOKEN, and local RunComfy configuration to execute model calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
