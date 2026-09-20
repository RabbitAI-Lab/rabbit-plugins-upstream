## Description:

Guides agents building or editing HyperFrames Studio projects on readable timeline layout, scene sub-compositions, caption tracks, element tracks, and safe-zone placement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content automation teams use this skill to structure HyperFrames projects so they open in Studio with readable, editable timelines and safe visual placement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect project structure can make HyperFrames Studio timelines harder to read and edit.

Mitigation: Run hyperframes lint, fix all findings, and open the project in Studio to verify the expected timeline rows.

Risk: The skill is specific to HyperFrames Studio project layout and may be inappropriate for unrelated editing tasks.

Mitigation: Use it only for HyperFrames Studio projects and rely on the core editing recipes for individual edit operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-studio)
- [HyperFrames core editing recipes](/hyperframes-core/references/creator-editing-recipes.md)
- [Sub-compositions reference](references/sub-compositions.md)
- [Embedded captions](/embedded-captions)
- [Preview safe margins source](packages/studio/src/utils/previewSafeMargins.ts)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code identifiers and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
