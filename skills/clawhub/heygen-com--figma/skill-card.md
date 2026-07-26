## Description: <br>
Import Figma content into a HyperFrames composition, including rendered assets, brand tokens, components, storyboard sections, connector-assisted motion when available, and shaders from a connector or native export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and motion designers use this skill to bring Figma designs, frames, logos, brand tokens, components, storyboards, animations, and shader assets into HyperFrames compositions while keeping render inputs local and repeatable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks the agent to silently update the skill package and related core skills before use. <br>
Mitigation: Require explicit user approval before updating installed skills or dependencies, and review the updated package before relying on it. <br>
Risk: Connector-assisted phases include telemetry or beacon behavior. <br>
Mitigation: Make telemetry clearly opt-in and explain when events are sent before running connector-assisted motion, shader, or storyboard workflows. <br>
Risk: Imported assets and raw connector responses can be stored locally in the project. <br>
Mitigation: Use a Figma token with only documented read-only scopes and avoid importing sensitive Figma content into projects where local storage is not acceptable. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands, generated local files, HTML components, JSON sidecars, and GSAP timeline code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Imports freeze Figma-derived assets locally; motion verification may use MP4 references and render outputs.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
