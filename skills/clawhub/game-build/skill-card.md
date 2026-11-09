## Description:

Builds a runnable game prototype or approved production game from an existing design and iterates it with replayable evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Game developers use this skill to prototype a high-risk design question or implement an approved game in its target runtime, with reproducible evidence for iteration and QA.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan was benign but incomplete because some referenced paths could not be matched, leaving evidence incomplete.

Mitigation: Review the referenced paths against the packaged files and assess whether the skill fits before installing; the scan does not guarantee the artifact is risk-free.

Risk: Blender scripts and third-party asset packages may run code with host-level effects.

Mitigation: Use only a verified local Blender service and do not execute embedded scripts from unreviewed third-party assets.

## Reference(s):

- [ClawHub release: 游戏构建执行 1.3.3](https://clawhub.ai/worldwonderer/skills/game-build)
- [Publisher profile: worldwonderer](https://clawhub.ai/user/worldwonderer)
- [Build brief contract](references/build-brief-contract.md)
- [Blender asset workflow](references/blender-asset-workflow.md)
- [Baked sprite workflow](references/baked-sprite-workflow.md)
- [Playable model contract](references/playable-model-contract.md)
- [TTS production contract](references/tts-production-contract.md)
- [Generative media pipeline](references/generative-media-pipeline.md)
- [Cutscene production](references/cutscene-production.md)

## Skill Output:

**Output Type(s):** [Code, Files, Markdown, Shell commands, Guidance]

**Output Format:** [Runnable game project files, BUILD_BRIEF.md, and replayable build or test evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Target platform, runtime, scope, and build stage follow the approved PRODUCT_BRIEF and design documents.]

## Skill Version(s):

1.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
