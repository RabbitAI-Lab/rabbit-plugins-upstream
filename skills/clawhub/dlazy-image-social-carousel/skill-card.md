## Description:

A structured workflow skill dedicated to social-media carousel design, using a single-confirmation and cover-first flow before generating the remaining slides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to plan and generate social-media carousel image sets with confirmed direction, a first approved cover, and visually consistent follow-up slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected media files, and generation parameters may be sent to dLazy cloud endpoints for processing.

Mitigation: Review prompts and selected files before generation, and use the skill only when cloud processing by dLazy is acceptable.

Risk: A dLazy API key may be stored in the local CLI configuration when using persistent login or auth setup.

Mitigation: Use the DLAZY_API_KEY environment variable or npx flow when persistent local credentials or a global CLI install are not desired.

Risk: Generated carousel images can include misleading, off-brand, or unsuitable design content if prompts are not reviewed.

Mitigation: Use the skill's direction-confirmation and cover-first approval steps before generating the remaining slides.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with confirmation tables, status updates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce hosted image URLs through the dLazy CLI after user confirmation.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
