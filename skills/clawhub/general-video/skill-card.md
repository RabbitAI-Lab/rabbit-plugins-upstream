## Description:

Author or edit custom HyperFrames compositions for longer or multi-scene videos, brand and sizzle reels, montages, static loops, title cards, footage remixes, and freeform builds when no specialized workflow fits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, video creators, and production teams use this skill to plan, build, edit, validate, preview, and optionally render HyperFrames video compositions when a more specialized workflow does not apply.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned HyperFrames commands and remote skill or catalog updates can change executable behavior after review.

Mitigation: Use the skill only where the HyperFrames npm package and hosted registry update path are trusted, or require a pinned or local HyperFrames CLI before execution.

Risk: The workflow can create and modify video project files and dispatch bounded scene workers for larger projects.

Mitigation: Run it in an expected project workspace, review generated brief, storyboard, composition, and motion files, and require HyperFrames checks before final preview or render.

Risk: Provider-backed media actions may require authentication or an offline fallback.

Mitigation: Check HyperFrames authentication status before provider actions and block or choose an available offline path when a required capability cannot be satisfied.

## Reference(s):

- [general-video ClawHub skill page](https://clawhub.ai/heygen-com/skills/general-video)
- [heygen-com publisher profile](https://clawhub.ai/user/heygen-com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, generated project files, HTML composition code, JSON motion sidecars, and validation output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify HyperFrames project files and can dispatch bounded scene-worker packets for larger projects.]

## Skill Version(s):

1.0.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
