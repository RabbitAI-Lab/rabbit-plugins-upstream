## Description: <br>
Creates original editorial illustrations, explainer diagrams, mini-comics, and transparent mascot cutouts where a recurring character performs the idea in one of the bundled looks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tmchow](https://clawhub.ai/user/tmchow) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, writers, and creative teams use Illo to turn articles, concepts, flows, and mascot requests into original illustration prompts and generated image artifacts. It supports article images, one-off concepts, explainer diagrams, mini-comics, character cutouts, custom mascots, community character packs, and backend/model selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill delegates user-derived prompts to general-purpose AI CLIs or OpenRouter with network access and workspace write access. <br>
Mitigation: Install and run it only in workspaces where those agent actions are acceptable, and review generated artifacts and proposed commands before relying on them. <br>
Risk: OpenRouter usage requires a credential and can incur pay-per-image charges. <br>
Mitigation: Keep API keys in the documented config file or platform secret store, avoid chat or command-line arguments for secrets, and require explicit paid fallback before spending. <br>
Risk: Community character pack installs and updates can change local character assets or behavior. <br>
Mitigation: Review character pack installs and updates before accepting them, especially in sensitive project directories. <br>


## Reference(s): <br>
- [Illo homepage](https://illo-skill.com) <br>
- [ClawHub skill page](https://clawhub.ai/tmchow/skills/illo) <br>
- [README](artifact/README.md) <br>
- [Backends - the three-backend image engine](artifact/references/backends.md) <br>
- [Composition](artifact/references/composition.md) <br>
- [Prompt recipe](artifact/references/prompt-recipe.md) <br>
- [Quality bar](artifact/references/quality-bar.md) <br>
- [Character builder](artifact/references/character-builder.md) <br>
- [Community character packs - install and publish](artifact/references/pack-sharing.md) <br>
- [Models - friendly names, ids, traits](artifact/references/models.md) <br>
- [Character cutout register](artifact/references/cutout.md) <br>
- [Surprise mode](artifact/references/surprise.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration directions, generated image file paths, and optional gallery artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate workspace image files through Codex, Grok, or OpenRouter backends; transparent cutouts require a cutout-capable backend.] <br>

## Skill Version(s): <br>
0.32.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
