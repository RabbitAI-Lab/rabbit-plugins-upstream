## Description:

Add word-timed captions to an Open Recut program by mapping the canonical transcript through timeline.json, reviewing maintained styles on source-backed pixels, rendering a local transparent HyperFrames PNG sequence, and registering it as an overlay contribution for the shared delivery render.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production agents use this skill to add reviewed, word-timed captions to Open Recut projects after video-understand has produced a validated transcript and timeline. It supports standard and expressive caption modes, style review, preview approval, and durable overlay registration for the final render.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow processes local video project files and writes caption plans, review pages, caches, overlay frames, and project registration data.

Mitigation: Run it only in the intended project workspace and review generated local pages before approving style choices, previews, or final overlay registration.

Risk: The workflow invokes ffmpeg, npx HyperFrames, and headless Chrome as part of local rendering and review generation.

Mitigation: Confirm those tools are expected in the environment and inspect generated evidence before accepting the rendered caption contribution.

Risk: The inspected artifact appears incomplete for referenced preview or font support assets.

Mitigation: Verify the installed package includes the referenced assets before relying on preview output or final overlay rendering.

Risk: Captions can conflict with later content cards or graphic motion if run in the wrong order.

Mitigation: Create captions before cards and graphics so the approved subtitle region can be preserved by later operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/whitetowerai/skills/video-add-captions)
- [Caption Rules and Data Shape](artifact/reference/caption-rules.md)
- [Caption Style Themes](artifact/reference/caption-style-themes.md)
- [Caption Feedback Mapping](artifact/reference/caption-feedback-mapping.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands plus generated JSON, SRT, HTML, PNG, and Markdown project artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local caption plans, interaction receipts, review pages, preview evidence, overlay frame sequences, and project registration data.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
