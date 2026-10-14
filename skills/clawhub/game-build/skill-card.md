## Description:

Builds a runnable game prototype or approved production candidate from game design and art direction, with a concise build brief and replayable verification evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Game developers and designers use this skill to turn an approved game design into a playable whitebox or production candidate, then document how to build and verify it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may change project-local game files and run build or verification commands.

Mitigation: Approve the game brief and review generated files and commands before running them.

Risk: Package managers, external media or voice services, and Blender integrations may introduce downloads, costs, or data-sharing concerns.

Mitigation: Review dependencies, provider permissions, licensing, and the data sent to services before enabling those steps.

## Reference(s):

- [ClawHub game-build release](https://clawhub.ai/worldwonderer/skills/game-build)
- [Build brief contract](artifact/references/build-brief-contract.md)
- [Playable model contract](artifact/references/playable-model-contract.md)
- [Blender asset workflow](artifact/references/blender-asset-workflow.md)
- [Generative media pipeline](artifact/references/generative-media-pipeline.md)
- [Voice production contract](artifact/references/tts-production-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Build brief, project files, and verification instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a runnable candidate when the required tools are available; otherwise provides a build brief without claiming the game was generated.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
