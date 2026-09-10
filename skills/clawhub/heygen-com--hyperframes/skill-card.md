## Description:

HyperFrames routes video, animation, motion-graphic, slideshow, captioning, PR-to-video, and Remotion migration requests into the appropriate HyperFrames workflow, including project inspection, validation, preview, render, publish, and batch-render operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and operators use HyperFrames to turn video-related requests into routed HyperFrames project workflows for creation, editing, validation, rendering, publishing, and migration. It is intended for agents that need to collect intent, select domain workflows, install or update required skills, and coordinate video production artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable remote npm/GitHub update commands can change project files or installed workflow skills.

Mitigation: Run the skill in a sandboxed project, limit filesystem and credential access, and review or pin CLI and workflow versions before allowing upgrades or skill refreshes.

Risk: Publishing and website capture workflows may expose project material or create hosted outputs.

Mitigation: Confirm source permissions, keep hosted outputs private by default, and review project artifacts before publishing or capture-heavy workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes)
- [Capability menu](references/capability-menu.md)
- [Intent interview](references/intent-interview.md)
- [Pitch round](references/pitch-round.md)
- [Skill installation and freshness](references/skill-lifecycle.md)
- [Workflow catalog](references/workflow-catalog.md)
- [Route briefs](references/route-briefs.md)
- [Route: general-video](references/routes/general-video.md)
- [Route: product-launch-video](references/routes/product-launch-video.md)
- [Route: pr-to-video](references/routes/pr-to-video.md)
- [Route: remotion-to-hyperframes](references/routes/remotion-to-hyperframes.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Agent guidance with Markdown references, shell commands, and project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update HyperFrames project files and invoke npm/GitHub-backed skill refreshes depending on the selected workflow.]

## Skill Version(s):

1.0.26 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
