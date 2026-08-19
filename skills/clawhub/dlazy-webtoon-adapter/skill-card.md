## Description:

Helps an agent adapt Chinese web novels into webtoon-ready story breakdowns, episode tags, and per-episode scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, writers, and agent users can use this skill to turn web-novel material into Chinese webtoon adaptation plans and script drafts. It also describes optional dLazy CLI use for hosted generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or invoke the dLazy CLI and can store an API key in local user configuration.

Mitigation: Use per-run DLAZY_API_KEY or npx when persistent global setup is not desired, and review any install or authentication command before running it.

Risk: Prompts and referenced media files may be sent to dLazy services for hosted processing.

Mitigation: Use the workflow only for content that is appropriate to send to dLazy, and confirm each generation command before execution.

Risk: The security scan marked the release suspicious because writing guidance is mixed with terminal-based image generation behavior.

Mitigation: Review the disclosed CLI behavior and API endpoints before deployment, especially in environments with strict data-handling or command-execution controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with structured Chinese prose and optional bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written to the conversation; generation commands may invoke the dLazy CLI when the user confirms them.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
