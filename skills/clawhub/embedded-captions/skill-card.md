## Description:

Embedded Captions helps agents add readable or cinematic captions to existing single-subject talking-head videos using identity-driven layouts, local transcription, subject matting, preview checks, and render/composite commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production agents use this skill to select a caption identity, generate project configuration, run local transcription and matting steps, preview visual fit, and render final captioned talking-head video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to run a silent self-update before use.

Mitigation: Review or remove the self-update step before deployment, and pin the exact skill version used in production workflows.

Risk: The workflow can retrieve packages, model weights, or browser-rendered assets from the network.

Mitigation: Use pinned local dependencies, bundle required runtime assets such as GSAP, and pre-stage model weights in a controlled environment.

Risk: The workflow processes user video and audio locally, which may include sensitive media.

Mitigation: Run the skill in a dedicated project directory with appropriate access controls, and avoid processing sensitive videos unless the local environment is approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption identity catalog](CATALOG.md)
- [Theme registry](themes/README.md)
- [Cinematic DNA registry](dna/README.md)
- [Rail caption guidance](references/rail.md)
- [Composition craft guidance](references/composition-craft.md)
- [Failure modes](references/failure-modes.md)
- [GSAP runtime CDN reference](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration files, generated HTML/composition files, preview frames, and final video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local project artifacts for caption planning, preview, validation, rendering, and compositing.]

## Skill Version(s):

1.0.9 (source: server release evidence, created 2026-08-11T18:58:49Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
