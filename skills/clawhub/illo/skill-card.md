## Description:

Creates original editorial illustrations, explainer diagrams, mini-comics, and transparent mascot cutouts in bundled visual styles from concepts, articles, URLs, or surprise prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tmchow](https://clawhub.ai/user/tmchow)

### License/Terms of Use:

MIT

## Use Case:

External creators, developers, and teams use illo to turn concepts, articles, or social posts into house-style editorial artwork, explainer images, mini-comics, or reusable mascot cutouts through an agent-guided image generation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-controlled prompts and references may be sent to the selected image-generation backend.

Mitigation: Review prompts and reference images before generation, and choose a backend whose data handling and cost model are acceptable for the workspace.

Risk: The skill can write illo configuration and character-pack files under the user's config directory.

Mitigation: Run setup and pack update commands only when intended, and inspect local config or pack changes before relying on them.

Risk: Autonomous local agent transports may have write ability, including an auto-approved path called out by the security scan.

Mitigation: Prefer a direct backend or carefully reviewed prompts when secondary agent execution is not acceptable.

Risk: Paid OpenRouter fallback can incur cost if explicitly enabled.

Mitigation: Do not use paid fallback unless the user has approved it and the backend selection is clear.

## Reference(s):

- [Illo homepage](https://illo-skill.com)
- [README](README.md)
- [Backend guide](references/backends.md)
- [Composition guide](references/composition.md)
- [Cutout guide](references/cutout.md)
- [Character builder](references/character-builder.md)
- [Pack sharing](references/pack-sharing.md)
- [Prompt recipe](references/prompt-recipe.md)
- [Quality bar](references/quality-bar.md)
- [Model guide](references/models.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, generated image file paths, and chat attachment directives when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local illo configuration, character packs, galleries, and generated image files depending on the selected workflow.]

## Skill Version(s):

0.34.3 (source: frontmatter and server release metadata, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
