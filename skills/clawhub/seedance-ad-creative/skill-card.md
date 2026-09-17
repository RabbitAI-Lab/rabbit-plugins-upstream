## Description:

Generates a cinematic product or brand ad video workflow from a product description or photo, including a creative brief, timestamped prompt, cost estimate, and Ofox video submission guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill to turn product descriptions or product photos into commercial-style brand video prompts and Ofox generation runs with explicit cost review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill delegates paid API execution to a separate external core skill and can incur charges.

Mitigation: Install only a pinned and reviewed local copy of the required core skill, run dry-run checks first, and require explicit user approval before paid generation.

Risk: Product images, prompts, generated media metadata, and OFOX_API_KEY-mediated requests are handled by Ofox tooling.

Mitigation: Use the skill only when the user accepts that data flow, protect the OFOX_API_KEY, and avoid sharing sensitive product material without authorization.

Risk: Real-person or likeness-related video options can create rights and consent concerns.

Mitigation: Use likeness-related options only when the user confirms they have the necessary rights and authorization.

Risk: Broad unpinned global installation increases the review surface for third-party code.

Mitigation: Prefer a narrow install of only the required Ofox core dependency at a reviewed version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-ad-creative)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-ad-creative)
- [Ofox app and API keys](https://app.ofox.ai)
- [Ofox models catalog](https://api.ofox.ai/v1/models/catalog)
- [Core video skill](../ofox-video-core/SKILL.md)
- [Prompt structure reference](../ofox-video-core/references/prompt-structure.md)
- [Creative brief reference](../ofox-video-core/references/creative-brief.md)
- [API parameter reference](../ofox-video-core/references/api-params.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured creative-brief details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cost estimates, dry-run approval steps, generated video job identifiers, download instructions, and final cost reporting.]

## Skill Version(s):

1.13.4 (source: server release evidence, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
