## Description:

Add word-timed captions to an Open Recut program by mapping the canonical transcript through timeline.json, reviewing a maintained style on source-backed pixels, rendering a local transparent HyperFrames PNG sequence, and registering it as an overlay contribution for the shared delivery render.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production agents use this skill to add reviewed, word-timed caption overlays to Open Recut projects after transcript and timeline understanding are available. It supports style selection, source-backed preview approval, spatial-context-aware placement for eligible composites, and final overlay contribution registration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local video project files and runs media/rendering tools, including npx HyperFrames.

Mitigation: Review the disclosed commands and dependencies before installation, run the skill only in the intended project workspace, and confirm that local media processing is acceptable.

Risk: Caption timing, placement, or style choices could be wrong, unreadable, or visually conflict with source footage.

Mitigation: Use the structured source-backed review pages, inspect generated preview evidence, and require the documented approval flow before final rendering.

Risk: Missing preview, font, or runtime assets can prevent reliable caption review or rendering.

Mitigation: Verify that the package includes the referenced assets and run the bundled self-checks before relying on generated output.

## Reference(s):

- [video-add-captions ClawHub page](https://clawhub.ai/whitetowerai/skills/video-add-captions)
- [Caption rules and data shape](reference/caption-rules.md)
- [Caption style themes](reference/caption-style-themes.md)
- [Caption feedback mapping](reference/caption-feedback-mapping.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with PowerShell, Bash, JSON, HTML review pages, SRT captions, PNG overlay frames, and project configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local review artifacts, caption plans, optional spatial context, approval receipts, transparent image sequences, and overlay contribution metadata.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
