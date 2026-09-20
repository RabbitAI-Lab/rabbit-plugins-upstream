## Description:

Mandatory entry point for requests to create, edit, animate, render, inspect, validate, preview, publish, or batch-render HyperFrames video, animation, motion graphic, slideshow, or Remotion-port projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to route video, animation, motion graphic, slideshow, and HyperFrames project requests into the appropriate workflow, including creation, editing, validation, rendering, publishing, and Remotion migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can refresh workflow skills and upgrade project HyperFrames tooling from external packages, which creates supply-chain and project-mutation risk.

Mitigation: Review dynamic install and update behavior before deployment, run in a controlled workspace, and verify project changes after HyperFrames CLI upgrades.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes)
- [HyperFrames entry point](artifact/SKILL.md)
- [Intent interview](artifact/references/intent-interview.md)
- [Brief contract](artifact/references/brief-contract.md)
- [Skill lifecycle](artifact/references/skill-lifecycle.md)
- [General video route](artifact/references/routes/general-video.md)
- [Product launch video route](artifact/references/routes/product-launch-video.md)
- [Remotion to HyperFrames route](artifact/references/routes/remotion-to-hyperframes.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes work to HyperFrames workflows and may create or update project files during video production.]

## Skill Version(s):

1.0.31 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
