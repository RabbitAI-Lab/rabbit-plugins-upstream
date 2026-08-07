## Description: <br>
Generate songs, instrumentals, or lyrics-driven tracks through a structured OpenClaw-native workflow with anti-sparse prompt engineering and quality verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luischarro](https://clawhub.ai/user/luischarro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use Music Craft to turn a music request, original lyrics, or an instrumental brief into a structured music-generation workflow with backend routing, prompt validation, and quality checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, lyrics, reference URLs, or generated music instructions may be sent to a cloud provider when a cloud backend is selected. <br>
Mitigation: Confirm the selected backend before generation and avoid submitting private lyrics, proprietary prompts, private URLs, or unlicensed reference material unless the user accepts that provider processing. <br>
Risk: Local backend setup can download large models and write temporary or generated audio files on the user's machine. <br>
Mitigation: Confirm the backend, install/download action, approximate impact, and save location before setup or generation; avoid overwriting user-visible outputs without explicit confirmation. <br>
Risk: Commercial rights for generated audio depend on the selected model, provider account terms, and input material, not only on the MIT-0 skill bundle license. <br>
Mitigation: Verify the active backend/model license, account tier, output terms, and ownership or permission for lyrics, samples, voices, and reference audio before commercial release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luischarro/skills/music-craft) <br>
- [Homepage metadata](https://github.com/LuisCharro/skills/tree/main/publish/music-craft) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Setup and Pre-Flight](references/setup-and-preflight.md) <br>
- [ACE-Step Generation](references/acestep-generation.md) <br>
- [Other Backends](references/other-backends.md) <br>
- [Prompt Formula](references/prompt-formula.md) <br>
- [Quality, Rate Limits, and Revision](references/quality-and-revision.md) <br>
- [Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline commands, configuration snippets, JSON helper reports, and generated audio file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Selected music backends may produce audio files; bundled helpers may produce JSON reports for lyrics linting, stem extraction, remixing, ACE-Step polling, and lyrics-alignment checks.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter, release evidence, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
