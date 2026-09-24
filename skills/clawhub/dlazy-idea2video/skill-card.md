## Description:

Turns a user's idea into a video-production workflow that plans story, characters, portraits, scenes, shots, keyframes, shot videos, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a creative idea into a structured idea-to-video generation plan, canvas workflow, and dLazy CLI-backed media generation process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist a dLazy API key in the local CLI configuration.

Mitigation: Use the per-run DLAZY_API_KEY option when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and referenced media may be sent to dLazy API and file-hosting services.

Mitigation: Install and run the skill only when sharing those prompts or media with dLazy services is acceptable.

Risk: The skill combines canvas planning guidance with direct terminal execution of dLazy CLI commands.

Mitigation: Confirm whether the intended workflow is canvas-only planning or direct CLI generation before allowing command execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline command examples and canvas workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide dLazy CLI calls that send prompts and referenced media to dLazy services.]

## Skill Version(s):

1.3.23 (source: server release metadata; artifact frontmatter reports 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
