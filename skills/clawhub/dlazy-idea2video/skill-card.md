## Description:

Turns a user's idea into a staged video-production workflow from story and characters through scenes, shots, keyframes, generated shot videos, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and agents use this skill to convert a creative idea into a structured video generation workflow with story development, character references, shot planning, image keyframes, generated video clips, and final concatenation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can run dLazy CLI commands through an external npm package.

Mitigation: Review the @dlazy/cli package and version before installation, avoid elevated shells, and confirm each generation step before execution.

Risk: The dLazy CLI stores an API key locally for authenticated requests.

Mitigation: Prefer scoped API keys, keep local configuration access restricted to the current user, and rotate or revoke keys when no longer needed.

Risk: Prompts and selected media files may be sent to dLazy services for generation.

Mitigation: Do not provide sensitive prompts or media unless the deployment owner accepts the data handling posture.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI Source Repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and structured workflow descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce canvas workflow shapes and invoke external dLazy video-generation services through the dLazy CLI.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
