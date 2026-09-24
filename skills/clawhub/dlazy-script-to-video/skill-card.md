## Description:

Turns scripts, screenplays, and shot lists into storyboarded, shot-by-shot videos by using the dLazy storyboard workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and video production teams use this skill to turn a script or scene breakdown into a multi-shot animated video workflow with consistent characters, prompts, generated shots, audio, subtitles, assembly, and validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy hosted services.

Mitigation: Avoid submitting sensitive data unless approved for the dLazy service and the relevant organization policy.

Risk: Authentication stores a revocable dLazy API key in the local user configuration.

Mitigation: Use OS-user access controls, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill relies on a pinned third-party CLI and hosted sandbox agent.

Mitigation: Review the pinned package and source before deployment, and run the CLI with the documented storyboard or project flags.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy CLI commands for authentication, project discovery, starting storyboard jobs, continuing projects, and attaching files.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
