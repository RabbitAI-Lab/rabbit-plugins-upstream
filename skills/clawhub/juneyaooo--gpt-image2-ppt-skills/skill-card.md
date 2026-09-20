## Description:

Generates polished presentation decks with OpenAI gpt-image-2, using built-in styles or a user-supplied PPTX template, and returns high-resolution slide PNGs plus a 16:9 PPTX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juneyaooo](https://clawhub.ai/user/juneyaooo)

### License/Terms of Use:

Apache 2.0

## Use Case:

External users, developers, and agent users use this skill to create, clone, and edit presentation decks from natural-language requests, outlines, existing templates, and source assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes a full-auto Codex fallback, broad installation effects, and unsafe handling patterns that deserve review before installation.

Mitigation: Review the skill before installing, avoid elevated privileges, and install dependencies in a virtual environment on shared or high-trust machines.

Risk: Persistent API-key configuration can expose credentials beyond the intended scope.

Mitigation: Use system or agent secret management and avoid storing real API keys in persistent agent config unless that scope is intended.

Risk: OpenAI-compatible endpoints return image URLs that are fetched by the host.

Mitigation: Prefer the direct OpenAI API path and use only trusted OpenAI-compatible endpoints.

Risk: Generated slides, especially data-heavy slides with small text or numbers, may need human verification before delivery.

Mitigation: Review final slide images and PPTX outputs, with extra checks for numbers, dense tables, legal text, and brand-sensitive assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juneyaooo/skills/gpt-image2-ppt-skills)
- [Source repository](https://github.com/JuneYaooo/gpt-image2-ppt-skills)
- [English README](https://github.com/JuneYaooo/gpt-image2-ppt-skills/blob/ce4714225d938b02806af3660a46e62be8900e29/docs/README.en.md)
- [Editing capability guide](https://github.com/JuneYaooo/gpt-image2-ppt-skills/blob/ce4714225d938b02806af3660a46e62be8900e29/docs/edit_guide.md)
- [Distilled style library](https://github.com/JuneYaooo/gpt-image2-ppt-skills/blob/ce4714225d938b02806af3660a46e62be8900e29/docs/distilled-styles.md)
- [OpenAI Images API documentation](https://platform.openai.com/docs/guides/images)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown instructions, JSON slide plans, shell commands, PNG slide images, and PPTX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use OpenAI-compatible image APIs and local PPTX renderers for template cloning or editable-output review.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
