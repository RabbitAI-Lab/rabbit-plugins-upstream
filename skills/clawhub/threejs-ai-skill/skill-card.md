## Description: <br>
Guides agents to produce coherent Three.js, WebGL, and react-three-fiber scenes by checking model normalization, layout, camera framing, lighting, collisions, controls, animation, and version-sensitive APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luisnavarrete12](https://clawhub.ai/user/luisnavarrete12) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when creating, reviewing, refactoring, or debugging Three.js, WebGL, and react-three-fiber scenes or games so generated code produces visually coherent, playable 3D output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated 3D scenes may compile while still rendering with incorrect scale, orientation, camera framing, lighting, collisions, or movement. <br>
Mitigation: Apply the skill's pre-flight checklist and visually verify the scene before relying on the output. <br>
Risk: Three.js API changes can make older examples or generated code use outdated renderer, lighting, or import patterns. <br>
Mitigation: Confirm the target Three.js version and adjust version-sensitive APIs before shipping generated code. <br>
Risk: Manual Three.js resources can leak GPU memory if a scene unmounts without disposal. <br>
Mitigation: Dispose geometries, materials, and textures during teardown and review custom resources that are not handled by framework caching. <br>
Risk: The artifact references additional guidance files that were not included in the release evidence. <br>
Mitigation: Treat missing reference files as unavailable and rely only on the included skill content unless the referenced files are separately verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luisnavarrete12/skills/threejs-ai-skill) <br>
- [Server-resolved GitHub repository](https://github.com/luisnavarrete12/threejs-ai-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions] <br>
**Output Format:** [Markdown guidance with inline code examples and implementation checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Three.js and react-three-fiber guidance for scene setup, model loading, camera controls, lighting, movement, animation, and visual verification.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
