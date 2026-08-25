## Description:

Creates original editorial illustrations, explainer diagrams, mini-comics, surprise-mode prompts, and transparent character cutouts using a recurring mascot and bundled visual styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tmchow](https://clawhub.ai/user/tmchow)

### License/Terms of Use:

MIT

## Use Case:

Creators, developers, and agents use Illo to turn concepts, articles, social posts, and workflows into original mascot-led editorial images or cutout assets with consistent visual style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or reference images may be sent to external image services or the user's logged-in Codex/Grok CLI.

Mitigation: Avoid sensitive inputs unless the selected backend is approved for them, and review prompts and reference images before generation.

Risk: Paid fallback can incur image-generation charges.

Mitigation: Use paid fallback only when the user explicitly intends to spend money.

Risk: Community character packs can change the visual identity and behavior of generated outputs.

Mitigation: Review community packs before installing or updating them.

Risk: The skill can write generated images, local character-pack files, and configuration files.

Mitigation: Run it in an expected workspace and review file paths before relying on generated assets.

## Reference(s):

- [Illo homepage](https://illo-skill.com)
- [README](README.md)
- [Composition guide](references/composition.md)
- [Backend guide](references/backends.md)
- [Character builder](references/character-builder.md)
- [Cutout guide](references/cutout.md)
- [Pack sharing](references/pack-sharing.md)
- [Quality bar](references/quality-bar.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, configuration notes, and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write generated image files and local character-pack or configuration files.]

## Skill Version(s):

0.35.0 (source: SKILL.md frontmatter and server release metadata, released 2026-08-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
