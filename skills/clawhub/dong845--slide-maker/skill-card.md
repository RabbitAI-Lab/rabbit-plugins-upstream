## Description: <br>
Builds, redesigns, and critiques presentation-grade slide decks for research, business, teaching, conference, stakeholder, and other presentation needs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dong845](https://clawhub.ai/user/dong845) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, educators, and business users use this skill to plan, build, redesign, render, lint, and review slide decks from source material or user direction. It emphasizes audience discovery, source fidelity, visual design quality, and an actor-critic review loop before handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local Python helpers may execute deck-supplied style.py, section.py, manifests, or direction-preview inputs. <br>
Mitigation: Run the skill only with trusted deck inputs, review generated Python and manifests before execution, and avoid executing third-party deck files without inspection. <br>
Risk: The skill can fetch web assets and use image-generation paths, including a metered OpenAI API path when configured. <br>
Mitigation: Review network and API use before running helper scripts, require explicit approval for metered API use, and verify licensing or provenance for sourced visual assets. <br>
Risk: The skill writes to Downloads and local caches and may keep a persistent taste profile across decks. <br>
Mitigation: Inspect output paths before handoff, run in a workspace appropriate for generated files, and review or delete ~/.codex/slide-templates/taste.md if cross-deck personalization is not desired. <br>
Risk: One image-generation path reads local Codex session files to recover generated image output. <br>
Mitigation: Avoid sensitive prompt content when using that path, or use an alternative image-generation workflow when local session-file access is not acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dong845/skills/slide-maker) <br>
- [Project details link from server skill summary](https://github.com/addsumtech/slides_maker) <br>
- [File inventory](artifact/references/file-inventory.md) <br>
- [Design principles](artifact/references/design-principles.md) <br>
- [Review rubrics](artifact/references/review-rubrics.md) <br>
- [Image generation guidance](artifact/references/image-generation.md) <br>
- [Codex runtime adapter](artifact/references/codex-runtime.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell code blocks; generated presentation artifacts when executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce .pptx decks, PDFs, rendered PNG previews, HTML previews, critique JSON, local cache entries, and reusable style/template files.] <br>

## Skill Version(s): <br>
4.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
