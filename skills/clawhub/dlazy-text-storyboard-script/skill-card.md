## Description:

Turns a theme, outline, or structured copy into a shot-by-shot short-video storyboard with filming directions and the original spoken script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to break short-video copy into filmable shots while preserving the supplied narration word for word.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes text-only storyboarding but also directs agents toward cloud image generation.

Mitigation: Review and approve any media-generation step separately; do not assume it is needed to produce the storyboard.

Risk: Using the dLazy CLI can store an API key locally and send prompts or referenced media to dLazy cloud services.

Mitigation: Install or authenticate only when needed, and do not supply credentials, secrets, or confidential scripts or media unless you intend them to be processed by that service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI repository (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown storyboard with video settings and numbered shots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each shot includes a scene, camera directions, filming notes, and verbatim spoken script.]

## Skill Version(s):

1.2.23 (source: ClawHub release record; embedded skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
