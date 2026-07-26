## Description: <br>
Aholo OpenAPI v1 global 3D tasks (reconstruction/generation): upload, create (worldId), poll/status. Gateway api.aholo3d.com, /global/world/v1. Default one create per single intent; multiple creates allowed when user explicitly chooses separate 3DGS per video. Not for 2D. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaohao17501671450-lgtm](https://clawhub.ai/user/xiaohao17501671450-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to upload selected media to Aholo and create, check, poll, or list 3D reconstruction and generation tasks that return worldId-based 3DGS results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated task requests use an under-disclosed beta API endpoint. <br>
Mitigation: Confirm that api-beta.aholo3d.com is the intended endpoint before installing or using the skill. <br>
Risk: Using the skill uploads selected media and uses an Aholo API key for tasks that may consume paid credits. <br>
Mitigation: Run create actions only after the user confirms the intended 3D task, and avoid duplicate create requests for the same intent. <br>
Risk: Disabling TLS verification weakens network protection. <br>
Mitigation: Prefer a trusted CA bundle and do not set AHOLO_INSECURE_SKIP_VERIFY unless the user accepts the network risk. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiaohao17501671450-lgtm/skills/aholo-3dgs-recon-global) <br>
- [Aholo API keys](https://labs.aholo3d.com/api-keys) <br>
- [Aholo pricing](https://www.aholo3d.com/pricing) <br>
- [Aholo 3DGS model viewer](https://studio.aholo3d.com/3dgs-model/{worldId}) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown status text with inline shell commands and links to generated 3D task results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include worldId, viewer URL, task status, poll metadata, and result file URLs such as PLY, SPZ, SOG, LOD metadata, or panorama output.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
