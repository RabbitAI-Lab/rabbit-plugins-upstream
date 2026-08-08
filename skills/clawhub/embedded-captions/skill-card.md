## Description:

Embedded Captions helps agents add readable or cinematic captions to single-subject talking-head videos by choosing a visual identity, preparing transcription and matting, authoring caption configuration, previewing, and rendering a final captioned video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and video-production agents use this skill to add verbatim subtitle rails, embedded caption peaks, or themed caption treatments to talking-head clips while leaving the underlying footage largely unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill silently updates installed skills and uses network-loaded or runtime code despite claiming local-only operation.

Mitigation: Require explicit approval before running network-backed updates, including npx hyperframes skills update and hyperframes init update behavior.

Risk: The workflow may download packages, models, or runtime code during preparation and rendering.

Mitigation: Require explicit approval for uvx package downloads, model downloads, and CDN access before execution.

Risk: Generated captions can be inaccurate when transcription quality is poor or speech is ambiguous.

Mitigation: Review the generated transcript and final captions when verbatim accuracy matters.

Risk: Media-processing scripts operate on project directories and video assets selected by the agent or user.

Mitigation: Run the workflow only in trusted project directories with intended input media.

## Reference(s):

- [Embedded Captions Catalog](CATALOG.md)
- [Rail Track Guidance](references/rail.md)
- [Composition Craft](references/composition-craft.md)
- [Theme Mode](themes/README.md)
- [Failure Modes](references/failure-modes.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell commands and JSON configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated project files and rendered captioned video artifacts when the agent runs the referenced local workflow.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
