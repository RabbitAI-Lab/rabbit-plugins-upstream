## Description:

Builds a risk-matched whitebox or production game from an approved design and delivers a runnable candidate for its target runtime.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers use this skill to turn approved design documents into a focused prototype or a complete playable build, then iterate against replayable evidence. It requires GAME_DESIGN.md, and ART_DIRECTION.md for production builds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates or modifies game files and runs project checks; generated code and selected dependencies may need separate review.

Mitigation: Provide the approved design documents first, review project changes and generated code, and assess selected dependencies before relying on them.

Risk: Optional media services may receive relevant assets or dialogue and may incur costs.

Mitigation: Confirm service permissions and costs before use, and send only the assets or dialogue needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/game-build)
- [Build brief contract](references/build-brief-contract.md)
- [Playable model contract](references/playable-model-contract.md)
- [Blender asset workflow](references/blender-asset-workflow.md)
- [Generative media pipeline](references/generative-media-pipeline.md)
- [Cutscene production](references/cutscene-production.md)
- [TTS production contract](references/tts-production-contract.md)
- [Baked sprite workflow](references/baked-sprite-workflow.md)

## Skill Output:

**Output Type(s):** [Files, Code, Markdown, Shell commands]

**Output Format:** [A Markdown build brief, runnable game project files, and commands for building, starting, and verifying the candidate.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The deliverable matches the whitebox or production stage; production includes a complete playable loop and an authoritative verification entry.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
