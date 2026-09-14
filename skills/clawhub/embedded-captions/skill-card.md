## Description:

Adds verbatim, cinematic, or themed captions to existing single-subject talking-head videos while preserving the underlying footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to select a caption identity, prepare transcription and subject matting, author caption configuration, preview visual QA frames, and render a captioned talking-head video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports under-scoped update and rendering paths that can execute code outside the reviewed artifact.

Mitigation: Install and run only from trusted publishers and trusted project directories; review proposed updates before allowing global skill updates.

Risk: The security guidance calls out theme DNA path validation and shell-script generation concerns.

Mitigation: Run projects in a sandbox with restricted filesystem and network access, and inspect generated commands before execution.

Risk: The security guidance calls out remote CDN script loading.

Mitigation: Restrict network access or vendor and pin remote browser dependencies before production use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Catalog](CATALOG.md)
- [Theme Mode](themes/README.md)
- [DNA Registry](dna/README.md)
- [Rail Track](references/rail.md)
- [Composition Craft](references/composition-craft.md)
- [Failure Modes](references/failure-modes.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local video-rendering plans, QA guidance, and render commands; final media files are created by the referenced local pipeline.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
