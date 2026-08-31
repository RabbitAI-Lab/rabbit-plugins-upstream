## Description:

Turns a user's idea into a video-production workflow covering story, characters, portraits, scenes, shots, keyframes, shot videos, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to turn a creative seed into a review-gated video generation plan and canvas workflow using dLazy services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy services for generation.

Mitigation: Avoid sensitive prompts and files, and review inputs before running generation commands.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use an environment variable or rotate and revoke stored keys when long-lived local credentials are not acceptable.

Risk: The skill can ask the agent to run dLazy CLI commands.

Mitigation: Require explicit user review before terminal execution and prefer npx when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured plan summaries, inline commands, and generated workflow data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces review-gated plan summaries before expanding the workflow; generated media is returned through dLazy-hosted URLs.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter lists 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
