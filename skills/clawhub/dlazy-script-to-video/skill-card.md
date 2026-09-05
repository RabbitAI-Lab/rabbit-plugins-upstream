## Description:

Turns scripts, screenplays, or shot lists into storyboarded, shot-by-shot video projects by breaking down scenes, generating shots, assembling them, and validating the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they have a script, screenplay, scene breakdown, or reference media and want an agent to drive dLazy's storyboard workflow for a multi-shot animated video with consistent characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files are sent to dLazy's hosted service.

Mitigation: Avoid attaching sensitive private media or confidential prompts unless the user intends to upload them to dLazy.

Risk: Authentication can persist a dLazy API key in the local CLI configuration.

Mitigation: Use local credential controls, rotate or revoke organization API keys when needed, and prefer per-invocation environment variables where persistence is undesirable.

Risk: Video generation depends on third-party dLazy API and file-storage endpoints.

Mitigation: Install only when use of the dLazy hosted service is acceptable and review service availability, account balance, and terms before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and terminal-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to invoke the pinned dLazy CLI storyboard workflow and may return streamed hosted-service responses.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
