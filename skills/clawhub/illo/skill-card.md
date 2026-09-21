## Description:

Illo helps agents create original editorial illustrations, explainer diagrams, mini-comics, and transparent mascot cutouts in bundled visual styles using configurable character packs and image backends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tmchow](https://clawhub.ai/user/tmchow)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, and agent users invoke Illo when they need a generated image that explains an article, concept, sequence, labeled process, or mascot cutout in a consistent house style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local commands and writes its own configuration under ~/.config/illo.

Mitigation: Install it only in environments where local command execution is acceptable, and review generated shell commands before running them.

Risk: Image generation sends prompts and reference images to the backend selected by the user or environment.

Mitigation: Avoid sending sensitive text, private artwork, or confidential reference images unless that backend is approved for the use case.

Risk: OpenRouter setup can involve API keys and paid image generation.

Mitigation: Let the user run initialization for secrets, avoid pasting keys in chat, and enable paid fallback only when the user explicitly wants it.

Risk: Community character packs may change the behavior or visual assets used by generated images.

Mitigation: Review community packs before installing, updating, or using them in production workflows.

## Reference(s):

- [Illo homepage](https://illo-skill.com)
- [ClawHub skill page](https://clawhub.ai/tmchow/skills/illo)
- [README](README.md)
- [Composition](references/composition.md)
- [Backends](references/backends.md)
- [Character Builder](references/character-builder.md)
- [Cutout](references/cutout.md)
- [Models](references/models.md)
- [Quality Bar](references/quality-bar.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated image file paths or attachments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may produce image-generation prompts, config guidance, gallery recommendations, and references to generated image artifacts.]

## Skill Version(s):

0.36.0 (source: frontmatter and release evidence, released 2026-09-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
