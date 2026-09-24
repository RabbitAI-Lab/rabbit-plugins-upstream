## Description:

Translate text, Markdown, or subtitle files with Yaps while preserving source files and subtitle timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to translate text, Markdown, and subtitle files through a local Yaps installation while preserving source files and timing-sensitive structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes broad Yaps CLI passthrough beyond the advertised translation-only purpose.

Mitigation: Review requested actions before execution and keep usage to translation workflows unless the user explicitly asks for another Yaps operation.

Risk: Yaps can create media-derived artifacts, Yaps projects, and normal local app history or project state.

Mitigation: Select only requested files, preserve source files, use new output filenames, and install only when local Yaps invocation and retained app state are acceptable.

## Reference(s):

- [Running Yaps from a local agent](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)
- [ClawHub skill page](https://clawhub.ai/yaps/skills/yaps-translation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated translated text or files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source files, uses new output filenames, and requires verification of subtitle cue indexes and timestamps.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
