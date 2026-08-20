## Description:

Author or edit custom HyperFrames compositions for longer or multi-scene videos, brand and sizzle reels, montages, static loops, static title cards, footage remixes, and companion-flow builds when no specialized workflow fits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to guide an agent through custom HyperFrames video creation or edits when a specialized workflow is not a fit. It supports companion-mode direction, multi-scene planning, media setup, validation checks, preview approval, and optional render handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can write or update HyperFrames project files.

Mitigation: Review BRIEF.md, STORYBOARD.md, generated compositions, and the final preview before approving a render.

Risk: Authenticated media providers may require sign-in or introduce billing-sensitive actions.

Mitigation: Check provider authentication status before the first authenticated action, review any sign-in or billing prompt, and choose an offline path when acceptable.

Risk: Large multi-scene projects may dispatch bounded scene workers that produce scene HTML and motion sidecars.

Mitigation: Use packet-bounded dispatch, wait for the expected composition and motion files, then run the HyperFrames checks before preview or render.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/general-video)
- [Publisher profile](https://clawhub.ai/user/heygen-com)

## Skill Output:

**Output Type(s):** [Markdown, Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, plus HyperFrames HTML, Markdown, and JSON project files when executing a build.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write BRIEF.md, STORYBOARD.md, composition HTML, and motion sidecar JSON; render occurs only after final preview approval.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
