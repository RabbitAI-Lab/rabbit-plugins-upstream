## Description: <br>
Turns a reference photo or text prompt into a textured GLB 3D mesh for game engines, AR scenes, product viewers, or 3D printing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical artists, and asset-production teams use this skill to plan and run image-to-3D or text-to-3D generation workflows that produce GLB meshes with topology, material, and polygon-budget settings matched to the target use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Chosen images or text prompts may be sent to Runware-compatible model tools. <br>
Mitigation: Avoid sensitive private images unless that provider workflow is acceptable for the intended use case. <br>
Risk: Provider model calls may incur usage costs. <br>
Mitigation: Confirm the selected model, settings, and expected cost before running generation. <br>
Risk: Model schemas and allowed settings differ by provider and model. <br>
Mitigation: Confirm the live model schema before sending requests, and do not reuse settings across models without checking compatibility. <br>


## Reference(s): <br>
- [Image-to-3D asset worked recipes](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, JSON] <br>
**Output Format:** [Markdown guidance with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces asynchronous 3dInference request guidance and GLB result-handling notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
