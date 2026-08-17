## Description:

Creates original editorial illustrations, explainer diagrams, mini-comics, transparent character cutouts, and surprise-mode image prompts using a recurring mascot and bundled visual styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tmchow](https://clawhub.ai/user/tmchow)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and creative teams use this skill to turn concepts, articles, brand ideas, or character requests into guided illustration workflows and generated image assets. It helps an agent choose a register, style, character, palette, model path, and delivery format for editorial art.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses network image-generation services and may send prompts, article text, or selected references to a configured backend.

Mitigation: Use explicit backend choices, avoid sensitive source material unless approved, and review prompts before generation in higher-risk contexts.

Risk: The skill can delegate generation to logged-in Codex or Grok command-line agents using the user's subscription context.

Mitigation: Run only in trusted workspaces, verify the selected backend before use, and avoid auto-approval flows where review is required.

Risk: Community character packs can be installed or updated persistently.

Mitigation: Review character packs and their sources before installing or updating them, and treat fetched packs as untrusted input.

Risk: OpenRouter use depends on a local configuration file containing an API key.

Mitigation: Let the user initialize or provision the key, keep the config file permission-restricted, and avoid exposing the key in prompts or command arguments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tmchow/skills/illo)
- [Illo homepage](https://illo-skill.com)
- [README](README.md)
- [Composition guide](references/composition.md)
- [Backend guide](references/backends.md)
- [Quality bar](references/quality-bar.md)
- [Character builder](references/character-builder.md)
- [Pack sharing](references/pack-sharing.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image file paths when rendering succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local image files through configured Codex, Grok, Grok Bot, or OpenRouter image-generation paths.]

## Skill Version(s):

0.34.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
