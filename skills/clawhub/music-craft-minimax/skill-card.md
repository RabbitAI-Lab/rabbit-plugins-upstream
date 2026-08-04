## Description: <br>
MiniMax-native music generation for OpenClaw: cover and style transfer that preserves melody, two-song mashups, AI lyrics generation and edit, emotion-driven prompt engineering, and per-flag mmx CLI control over BPM, key, structure, and avoid lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luischarro](https://clawhub.ai/user/luischarro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, music producers, and OpenClaw users use this skill to plan and run MiniMax-backed music generation workflows, including covers, style transfer, mashups, lyrics generation, emotion analysis, and precision mmx flag control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, lyrics, and selected local audio may be sent to MiniMax cloud APIs when cloud generation or cover workflows are used. <br>
Mitigation: Confirm user consent and rights to upload the material before cloud generation; use local-only or no-advanced analysis paths when external transmission is not acceptable. <br>
Risk: The skill works with local audio paths and writes generated files, caches, and analysis artifacts. <br>
Mitigation: Run it in a scoped workspace, review requested paths before execution, and avoid using sensitive or unrelated local files as inputs. <br>
Risk: Optional remote-model-code behavior and git-based installs can expand the code execution surface. <br>
Mitigation: Avoid those options unless the referenced code or repository has been reviewed and is trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luischarro/skills/music-craft-minimax) <br>
- [Publisher profile](https://clawhub.ai/user/luischarro) <br>
- [ClawDIS homepage](https://github.com/LuisCharro/skills/tree/main/publish/music-craft-minimax) <br>
- [README](README.md) <br>
- [MiniMax generation caveats](references/minimax-generation-caveats.md) <br>
- [Cover workflow](references/cover-workflow.md) <br>
- [Quota checking](references/quota-checking.md) <br>
- [Error handling](references/error-handling.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, JSON analysis artifacts, and generated audio file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or reference MP3 audio outputs, local analysis JSON, lyric files, verification results, and loudness-finalized files during agent workflows.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter, release evidence, README, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
