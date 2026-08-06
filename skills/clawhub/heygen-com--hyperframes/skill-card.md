## Description: <br>
HyperFrames routes video, animation, motion graphic, slideshow, and Remotion-port requests into the appropriate HyperFrames workflow, resumes existing projects, and helps inspect, validate, preview, render, publish, or batch-render projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creative operators, and agent users use HyperFrames as the front door for creating or editing videos, motion graphics, presentations, captioned clips, product promos, music videos, PR explainers, and Remotion migrations. It turns the user's request into a routed HyperFrames workflow, project brief, and follow-on execution path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update HyperFrames CLI pins and install or refresh workflow skills, which may change project dependencies or installed skill behavior. <br>
Mitigation: For reproducibility-sensitive projects, require approval before upgrade or skills update operations, review resulting project changes, and run HyperFrames checks after any upgrade. <br>
Risk: Website capture, publish, and external provider operations can expose project inputs or outputs outside the local workspace. <br>
Mitigation: Confirm that the input content may be captured or sent to external services, and require explicit approval before publishing or using external provider operations. <br>
Risk: Automated routing and defaulted brief fields can select an unsuitable workflow or creative direction when the user request is ambiguous. <br>
Mitigation: Keep stated choices and inferred defaults separate in the brief summary, ask routing-only clarification when required, and require confirmation before executing an edited brief. <br>


## Reference(s): <br>
- [HyperFrames ClawHub page](https://clawhub.ai/heygen-com/skills/hyperframes) <br>
- [HyperFrames entry point](artifact/SKILL.md) <br>
- [Intent interview](artifact/references/intent-interview.md) <br>
- [Capability menu](artifact/references/capability-menu.md) <br>
- [Pitch round](artifact/references/pitch-round.md) <br>
- [Skill lifecycle](artifact/references/skill-lifecycle.md) <br>
- [Workflow route contracts](artifact/references/routes/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands, project brief content, and HyperFrames project file updates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes work to HyperFrames workflow skills that may produce project files, previews, rendered media, or published links.] <br>

## Skill Version(s): <br>
1.0.21 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
