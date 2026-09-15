## Description:

Guides an agent through avatar, outfit, motion, voice, background, and product-asset workflows for AI outfit-change, dance, runway, digital-human speaking, pose-video, and static asset generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to plan and execute structured AI media workflows that combine avatar, clothing, motion, lip-sync audio, backgrounds, and product props into reusable assets, static compositions, or short videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles portraits, voices, product images, and background assets that may be sensitive or require permission.

Mitigation: Require clear authorization for likeness, voice, copyrighted material, and brand or product assets before running lip-sync, digital-human, product-placement, or cloud-connector workflows.

Risk: Depth-model loading accepts local .pth weights, which can be unsafe if the weights are untrusted.

Mitigation: Use only model weights from trusted, verified sources and avoid arbitrary .pth files.

Risk: Cloud-connector workflows may process user assets outside the local environment.

Mitigation: Confirm where data will be processed before sending face, voice, product, or background assets to any external service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/avatar-outfit-motion-video)
- [avatar-outfit-motion-catalog.md](references/avatar-outfit-motion-catalog.md)
- [avatar-outfit-motion-requirements.md](references/avatar-outfit-motion-requirements.md)
- [avatar-outfit-motion-exemplars.md](references/avatar-outfit-motion-exemplars.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, asset plans, prompts, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated image, audio, video, and depth-map artifacts created by external tools.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
