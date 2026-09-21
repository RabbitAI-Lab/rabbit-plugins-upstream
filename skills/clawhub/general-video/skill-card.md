## Description:

Author or edit custom HyperFrames compositions for longer or multi-scene videos, brand reels, montages, static loops, title cards, footage remixes, and freeform builds when no specialized workflow fits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to plan, build, verify, and hand off HyperFrames video projects when a specialized video workflow does not apply or a companion co-creation flow is requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks the agent to run and update HyperFrames through unpinned npx commands, so behavior may change with the npm package or update channel.

Mitigation: Install only if the HyperFrames npm package and update channel are trusted; prefer a pinned, reviewed local HyperFrames CLI for controlled environments.

Risk: The workflow can run provider, catalog, validation, preview, and render commands while building video projects.

Mitigation: Review proposed commands before execution, gate authenticated provider actions, and inspect HyperFrames check results and final previews before rendering or publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/general-video)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce HyperFrames project files, storyboard materials, composition HTML, motion JSON sidecars, checks, previews, and render handoff details depending on the requested video task.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
