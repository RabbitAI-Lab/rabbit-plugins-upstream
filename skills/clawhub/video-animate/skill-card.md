## Description:

Turns an approved video previz, characters, moodboard, script, and locked sound into shot plans, model choices, prompt guidance, and footage ready for editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers and creative developers use this skill to plan and generate AI or code-assisted footage from an approved Blender or three.js previz, choosing a model and generation approach for each shot. It guides low-cost draft passes, take review, sound sync, and handoff to editing and motion design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creative media and prompts may be sent to external generation providers.

Mitigation: Before generating, check which providers receive the inputs and confirm you are authorized to share them.

Risk: Install examples use unpinned npx packages.

Mitigation: Review package sources and versions before installing.

Risk: The security scan is partial because some local references could not be resolved.

Mitigation: Treat the scan as incomplete and review the package sources and versions before use.

## Reference(s):

- [Routing shots between code, AI, or a hybrid approach](references/routing.md)
- [Model selection and route guidance](references/models.md)
- [Drafts, takes, and generation planning](references/drafts-and-takes.md)
- [Prompt patterns](references/prompts.md)
- [Sound sync guidance](references/sound-sync.md)
- [Preparing footage for editing and motion design](references/post-ready.md)
- [Animate a previz with AI video models](https://varg.ai/how-to/animate-a-previz-with-ai-video-models)
- [BytePlus ModelArk video model documentation](https://docs.byteplus.com/en/docs/ModelArk/2607689)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, JSON, Video files]

**Output Format:** [Markdown shot plans and prompts, shell commands, JSON take-check results, and generated video footage or plates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated footage depends on the selected external model and route; the skill also provides take measurements and handoff guidance.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
