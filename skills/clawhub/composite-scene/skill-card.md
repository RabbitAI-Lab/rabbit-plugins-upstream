## Description: <br>
Merge several real images into one coherent picture without manual cut-out or masking, using reference images and prompts to align placement, scale, lighting, and perspective. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to guide agents through composing multiple user-provided reference images into a single image, such as placing products in scenes, merging subjects, or applying a style reference while keeping relationships and lighting coherent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reference images may contain sensitive private content that would be sent to the configured image-generation provider. <br>
Mitigation: Use only images the user is comfortable sending to that provider, and avoid sensitive private images unless the provider handling is acceptable for the use case. <br>


## Reference(s): <br>
- [Worked recipes](references/examples.md) <br>
- [Composite Scene on ClawHub](https://clawhub.ai/runware/skills/composite-scene) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration] <br>
**Output Format:** [Markdown guidance with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to collect multiple reference images, confirm the live image model schema, and produce imageInference request shapes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
