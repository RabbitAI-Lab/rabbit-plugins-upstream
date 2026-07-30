## Description: <br>
HyperFrames routes video, animation, motion-graphics, slideshow, Remotion-port, and existing-project requests into the appropriate HyperFrames workflow, capturing intent and installing workflow or domain skills as needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill as the front door for creating, editing, validating, previewing, rendering, publishing, or batch-rendering HyperFrames video projects. It is intended for video, animation, motion-graphics, product-launch, PR-explainer, music-video, captioning, slideshow, and Remotion-migration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: URL-based product-video workflows may capture websites that the user is not authorized to capture or that contain private, authenticated, or sensitive content. <br>
Mitigation: Confirm permission to capture the target site before use and avoid authenticated, private, or sensitive pages unless the downstream tools explicitly support that use. <br>
Risk: Publishing workflows can create stable public links for rendered output. <br>
Mitigation: Review the rendered video and intended audience before publishing or sharing a public link. <br>
Risk: The skill manages workflow routing and invokes CLI-based setup, update, validation, rendering, and publishing commands. <br>
Mitigation: Install and run it only when HyperFrames should manage the project workflow, and treat failed install or update commands as visible tool failures. <br>


## Reference(s): <br>
- [ClawHub HyperFrames Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes) <br>
- [HyperFrames Entry Point](artifact/SKILL.md) <br>
- [Capability Menu](artifact/references/capability-menu.md) <br>
- [Intent Interview](artifact/references/intent-interview.md) <br>
- [Skill Installation and Freshness](artifact/references/skill-lifecycle.md) <br>
- [Workflow Route Contracts](artifact/references/workflow-catalog.md) <br>
- [Product Launch Video Route](artifact/references/routes/product-launch-video.md) <br>
- [General Video Route](artifact/references/routes/general-video.md) <br>
- [Remotion to HyperFrames Route](artifact/references/routes/remotion-to-hyperframes.md) <br>
- [Slideshow Route](artifact/references/routes/slideshow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes to specialized HyperFrames workflows; deliverables may include MP4, WebM, MOV, runnable HTML compositions, slideshow JSON, caption layers, or stable public links depending on the selected route.] <br>

## Skill Version(s): <br>
1.0.20 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
