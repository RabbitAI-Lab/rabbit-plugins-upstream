## Description: <br>
Advanced music generation for OpenClaw, using the MiniMax Music 2.6 token plan for cover and style transfer, two-song mashups, lyrics generation, emotion-driven prompt engineering, and fine control through the mmx CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luischarro](https://clawhub.ai/user/luischarro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creative operators, and agent users use this skill to plan, lint, run, and verify MiniMax-powered music workflows such as covers, style transfer, mashups, lyrics generation, and emotion-informed prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud generation can send prompts, lyrics, and audio to MiniMax. <br>
Mitigation: Confirm user consent and rights before upload, and use local-only alternatives for sensitive audio where available. <br>
Risk: The workflow requires an operator-provided MiniMax API key. <br>
Mitigation: Use the operator's own MiniMax account and keep MINIMAX_API_KEY out of shared outputs, logs, and skill bundles. <br>
Risk: Local analysis and generation workflows can leave cache files or temporary media on shared machines. <br>
Mitigation: Clear or redirect ~/.cache/openclaw and nearby analysis cache files when working with private material. <br>
Risk: Optional unpinned git installs can change behavior over time. <br>
Mitigation: Prefer pinned dependencies or review optional tool installs before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luischarro/skills/music-craft-minimax) <br>
- [Declared homepage](https://github.com/LuisCharro/skills/tree/main/publish/music-craft-minimax) <br>
- [README](README.md) <br>
- [Setup and preflight](references/setup-and-preflight.md) <br>
- [MiniMax generation caveats](references/minimax-generation-caveats.md) <br>
- [Cover workflow](references/cover-workflow.md) <br>
- [Mashup workflow](references/mashup-workflow.md) <br>
- [Lyrics generation](references/lyrics-generation.md) <br>
- [Emotion analysis](references/emotion-analysis.md) <br>
- [mmx flags reference](references/mmx-flags-reference.md) <br>
- [Error handling](references/error-handling.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration notes, and generated audio-file verification steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local analysis JSON, lyrics text, prompt text, temporary media, and generated MP3 outputs when the agent runs the bundled workflows.] <br>

## Skill Version(s): <br>
1.5.1 (source: frontmatter, release evidence, README, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
