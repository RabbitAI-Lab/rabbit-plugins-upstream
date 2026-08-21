## Description:

Analyzes a short-video link, extracts the script and creative structure, and guides an agent through rewriting it for the user's product before generating a comparable LinkPix/qhkit marketing video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to adapt a viral Douyin or TikTok-style short video into a product-specific marketing video while preserving the source video's structure, pacing, and camera language. The skill also guides the agent to show rewritten scripts for review and request confirmation before any credit-spending generation step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt agents to install Node or qhkit globally in the execution environment.

Mitigation: Preinstall qhkit in a managed environment or require operator review before any global dependency installation.

Risk: The skill may automatically reuse a root-level qhkit API configuration.

Mitigation: Use a task-scoped token and avoid shared root-level credentials in multi-user or locked-down environments.

Risk: Video generation can spend credits and cannot be cancelled after submission.

Mitigation: Require explicit user confirmation of model, inputs, duration, reference media, and estimated credits before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-clone)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce rewritten scripts, command parameters, task IDs, status checks, credit estimates, and generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
