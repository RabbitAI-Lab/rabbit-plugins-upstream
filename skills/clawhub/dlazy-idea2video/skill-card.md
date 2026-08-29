## Description:

Turns a user's idea into a video-production workflow covering story, characters, portraits, scenes, shots, keyframes, shot videos, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to turn an initial video idea into a structured generation plan, canvas workflow, dLazy CLI generation steps, and final video assembly path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be sent to dLazy's cloud API and file service.

Mitigation: Use only prompts and media approved for dLazy cloud processing, and review referenced local files before generation.

Risk: The workflow may install or invoke the dLazy CLI and store a local API key.

Mitigation: Prefer npx or the DLAZY_API_KEY environment variable for temporary use, and rotate or revoke saved API keys when they are no longer needed.

Risk: The skill includes terminal execution steps after interactive planning.

Mitigation: Review each generated command and run only one confirmed dLazy generation command at a time.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON-like plan summaries and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce canvas workflow shapes and dLazy CLI calls that generate hosted image or video URLs.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
