## Description:

Creates original editorial illustrations where a recurring mascot character performs the idea, including single editorial scenes, explainer diagrams, transparent character cutouts, and surprise-mode image prompts across bundled visual looks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tmchow](https://clawhub.ai/user/tmchow)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to turn article ideas, concepts, or mascot-driven visual briefs into original editorial image assets and related setup guidance. It supports direct concept illustration, article image sets, explainer diagrams, transparent character cutouts, custom character packs, and model/backend selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local terminal commands for image generation.

Mitigation: Review the skill before deployment and install it only in environments where local command execution is acceptable.

Risk: The skill can call external image services and some backends may incur usage quota or paid image-generation costs.

Mitigation: Confirm the selected backend and require explicit approval for paid fallback or direct paid OpenRouter use.

Risk: Community character packs can be installed or updated into the user's configuration directory.

Mitigation: Review community packs before installing or updating them, and treat pack files as content rather than trusted instructions.

Risk: Publishing character packs can send user-created content to GitHub publicly.

Mitigation: Publish packs only when the user intends the content to be public and understands the associated licensing and attribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tmchow/skills/illo)
- [illo homepage](https://illo-skill.com)
- [Backends](references/backends.md)
- [Composition](references/composition.md)
- [Cutout](references/cutout.md)
- [Prompt Recipe](references/prompt-recipe.md)
- [Quality Bar](references/quality-bar.md)
- [Pack Sharing](references/pack-sharing.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, image files]

**Output Format:** [Markdown guidance with inline shell commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PNG or JPEG image assets, transparent cutouts when the selected backend supports alpha, and configuration files for backend and character preferences.]

## Skill Version(s):

0.33.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
