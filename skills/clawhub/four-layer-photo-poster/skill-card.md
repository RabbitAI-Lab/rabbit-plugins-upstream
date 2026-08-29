## Description:

Turn each supplied photo into its own 3:4 vertical, four-stage design poster with exact four-band assembly and a continuous source scene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT

## Use Case:

External creators and agents use this skill to transform each supplied source photo into an independent 3:4 four-band poster while preserving the source scene across photographic and stylized layers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied photos may contain sensitive personal or private visual information.

Mitigation: Review source photos and generated posters before sharing or deployment, and avoid using sensitive photos unless the user has approved the image-generation workflow.

Risk: Generated layers may alter identity, pose, scene details, or text despite the skill's constraints.

Mitigation: Inspect the assembled poster against the acceptance checklist, regenerate only the failed layer, and preserve the original photo band.

## Reference(s):

- [Layer prompts](artifact/references/production-prompt.md)
- [Server-resolved source repository](https://github.com/ToBeWin/four-layer-photo-poster)
- [ClawHub skill page](https://clawhub.ai/tobewin/skills/four-layer-photo-poster)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance with image-generation prompts and an assembled poster image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one 3:4 poster per supplied photo; default assembled output is 1200x1600.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
