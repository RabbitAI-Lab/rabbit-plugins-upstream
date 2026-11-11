## Description:

Animate an approved video previz into footage by choosing per-shot methods and models, testing at low resolution, and preparing takes for editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers and video creators use this agent skill to turn an approved Blender or three.js previz and locked soundtrack into AI-generated footage and edit-ready plates. It helps plan per-shot methods, models, takes, costs, and handoff materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference footage, images, or prompts may be processed by external media services.

Mitigation: Check each provider's privacy terms and avoid sending sensitive material unless its use is approved.

Risk: The documented npx installation command is unpinned, creating supply-chain uncertainty.

Mitigation: Review the package and source before installation, and use a verified pinned release where available.

Risk: Repeated video generations can consume paid credits beyond the intended budget.

Mitigation: Estimate each run's cost and agree on a spending cap before uploading assets or starting generations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vargai/skills/video-animate)
- [Project homepage](https://github.com/vargHQ/skills/tree/main/video-animate)
- [Routing guide](artifact/references/routing.md)
- [Model selection and pricing guide](artifact/references/models.md)
- [Drafts and takes guide](artifact/references/drafts-and-takes.md)
- [Sound synchronization guide](artifact/references/sound-sync.md)
- [Post-production handoff guide](artifact/references/post-ready.md)
- [Take metadata example](artifact/assets/take.example.json)
- [Take checker](artifact/scripts/take_check.py)
- [BytePlus video model guidance](https://docs.byteplus.com/en/docs/ModelArk/2607689)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Code]

**Output Format:** [Markdown plans and prompts, JSON take records, and shell commands with Python check output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces shot and run plans, edit-ready plates, and take handoff data; measured checks support but do not replace human review of the footage.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; skill frontmatter declares 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
