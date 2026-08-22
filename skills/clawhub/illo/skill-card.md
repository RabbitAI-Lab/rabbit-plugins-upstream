## Description:

Creates original editorial illustrations, explainer diagrams, mini-comics, and transparent character cutouts with a recurring mascot in bundled visual looks, using configured Codex, Grok, Grok Bot, or OpenRouter image-generation paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tmchow](https://clawhub.ai/user/tmchow)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use Illo to turn article URLs, post ideas, brand concepts, mascot prompts, or cutout requests into styled illustration assets and supporting generation commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run logged-in Codex or Grok CLI sessions in headless or auto-approved modes.

Mitigation: Install only when that behavior is acceptable, review generated commands before use, and prefer a dedicated workspace for untrusted prompts.

Risk: The OpenRouter backend can use a paid account and requires a locally stored API key.

Mitigation: Use the OpenRouter path only with explicit user consent, keep the key in the skill config or platform secret store, and avoid sharing the key in chat or command arguments.

Risk: Character pack installation or updates may apply external pack content.

Mitigation: Review pack content before installing or updating packs, especially from third-party sources.

Risk: Recurring update checks or automated backend fallback may be surprising in sensitive environments.

Mitigation: Leave recurring update checks disabled unless explicitly desired and require opt-in for paid fallback behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tmchow/skills/illo)
- [Illo homepage](https://illo-skill.com)
- [SKILL.md](artifact/SKILL.md)
- [README.md](artifact/README.md)
- [Backend reference](artifact/references/backends.md)
- [Composition reference](artifact/references/composition.md)
- [Cutout reference](artifact/references/cutout.md)
- [Model reference](artifact/references/models.md)
- [Pack sharing reference](artifact/references/pack-sharing.md)
- [Quality bar reference](artifact/references/quality-bar.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated image file paths or attachments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local image files, transparent PNG cutouts, galleries, and user-specific configuration files depending on the selected backend and request.]

## Skill Version(s):

0.34.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
