## Description: <br>
Generate music through a disciplined OpenClaw-native workflow for songs, instrumentals, and lyrics-driven tracks with structured prompt engineering and quality verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luischarro](https://clawhub.ai/user/luischarro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use this skill to turn music requests into production-sheet prompts, route them to an available music backend, generate audio, and verify the result before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, lyrics, reference URLs, or generated music instructions may be sent to a cloud music provider. <br>
Mitigation: Confirm the selected backend and explain what will leave the user's machine before uploading or generating with a cloud workflow. <br>
Risk: Local workflows may download models, write generated audio caches, or create temporary files. <br>
Mitigation: Ask for consent before large downloads or installs, confirm the output folder, and avoid overwriting existing outputs. <br>
Risk: Inputs or generated outputs may involve third-party lyrics, samples, voices, model terms, or non-commercial model weights. <br>
Mitigation: Confirm rights to input material and verify the selected backend, model license, account tier, and output terms before commercial use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luischarro/skills/music-craft) <br>
- [Project homepage](https://github.com/LuisCharro/skills/tree/main/publish/music-craft) <br>
- [README](README.md) <br>
- [ACE-Step generation guide](references/acestep-generation.md) <br>
- [Backend guide](references/other-backends.md) <br>
- [Setup and preflight](references/setup-and-preflight.md) <br>
- [Quality and revision](references/quality-and-revision.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with structured prompts, command snippets, configuration notes, and generated audio delivery instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or reference generated audio files through the selected local or cloud backend.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release, frontmatter, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
