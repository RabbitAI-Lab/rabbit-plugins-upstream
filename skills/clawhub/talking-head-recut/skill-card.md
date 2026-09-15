## Description:

Packages an existing talking-head, interview, or podcast video with transcript-synced graphic overlay cards while preserving the underlying clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, editors, marketers, and agents use this skill to dress an existing speaker video with timed titles, lower-thirds, quotes, data callouts, side panels, and picture-in-picture graphics. It is suited for packaging interviews, podcasts, and social clips where the original video should remain intact under designed overlays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may run unpinned npm/HyperFrames commands or update skill code before use.

Mitigation: Use a pinned and reviewed HyperFrames version, review any skill update diff before accepting it, and run the workflow in a controlled workspace.

Risk: The workflow processes local video, audio, and transcript files.

Mitigation: Use only media you are permitted to process, keep sensitive source footage in trusted storage, and review generated transcript and overlay content before rendering or sharing.

Risk: The optional preview or shareable server can expose generated media if started unnecessarily.

Mitigation: Start preview/shareable serving only when explicitly needed and stop it after review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/talking-head-recut)
- [NOTICE.md](NOTICE.md)
- [V-Take Visual Design Library](references/DESIGN_INDEX.md)
- [Layout References](references/layouts/)
- [Style References](references/styles/)
- [Frame References](references/frames/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON storyboard structure, HTML/CSS card fragments, and composition code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-authored project files such as metadata.json, transcript.json, storyboard.json, public/cards/*.html, public/index.html, and output.mp4 when executed in a video workspace.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
