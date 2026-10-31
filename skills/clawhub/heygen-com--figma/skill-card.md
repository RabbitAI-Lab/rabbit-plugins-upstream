## Description:

Bring Figma into a HyperFrames video - rendered assets, brand tokens, components, storyboard frames as reconstructed motion (frames read as states, not slides), shaders and connector-assisted motion. Use when the person pastes a figma.com link or asks to use a Figma design, frame, logo or brand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to bring Figma assets, brand tokens, components, motion, and storyboard states into HyperFrames video compositions. It also guides verification against Figma exports and handling of content that cannot be translated directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External HyperFrames CLI versions and privacy controls may change.

Mitigation: Use a reviewed, fixed HyperFrames version and verify its privacy controls before running commands.

Risk: Cached Figma data may contain private designs.

Mitigation: Keep cached private designs out of public repositories.

Risk: A Figma access token may have broader access than needed.

Mitigation: Use a read-only token with only the required scopes, and never paste it into chat.

## Reference(s):

- [ClawHub Figma skill release](https://clawhub.ai/heygen-com/skills/figma)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [SVG or PNG assets, editable HTML components, JavaScript timeline code, and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Imports are saved as local build-time assets; motion that cannot be translated may be frozen as video.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
