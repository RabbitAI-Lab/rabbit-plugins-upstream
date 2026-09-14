## Description:

Author or edit custom HyperFrames compositions for longer or multi-scene videos, companion-flow projects, brand reels, montages, loops, title cards, footage remixes, and other freeform video builds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-building agents use this skill to plan, author, verify, and optionally render HyperFrames compositions when a more specialized workflow does not fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned HyperFrames CLI commands and skill-update steps may execute or change remote code before the reviewed workflow runs.

Mitigation: Review updates before use, pin or otherwise control the HyperFrames CLI version, and run the workflow in a constrained project environment.

Risk: Provider-backed media operations may require authentication or credentials during video creation.

Mitigation: Use minimal credentials, check authentication state before provider actions, and prefer offline/local providers when they satisfy the requested capability.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, generated project files, HTML/CSS/JS composition code, JSON motion sidecars, and configuration files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce BRIEF.md, STORYBOARD.md, HyperFrames project files, composition fragments, motion sidecars, validation output, and a rendered video only after approval.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
