## Description:

视频生成 Video Generate selects an appropriate dLazy CLI video model for text-to-video, image-to-video, first/last-frame video, digital-human, and lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to choose and run dLazy CLI video-generation commands for prompts, images, reference media, digital-human video, and lip-sync workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill wraps a pinned dLazy npm CLI that sends prompts, parameters, and selected media files to dLazy hosted services.

Mitigation: Use an unprivileged sandbox or npx, review the pinned CLI package before use, and avoid sending media that should not leave the local environment.

Risk: Authentication may store an API key in a local dLazy config file.

Mitigation: Use a revocable API key or DLAZY_API_KEY for per-invocation credentials, rotate keys when needed, and avoid running npm or the CLI as root.

Risk: Generated results and uploaded media are handled through dLazy service endpoints.

Mitigation: Confirm the dLazy account, service terms, and data-handling expectations before using the skill for sensitive or regulated content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and references to JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to authenticate, inspect model-specific CLI flags, execute dLazy commands, and interpret returned hosted video URLs.]

## Skill Version(s):

1.4.17 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
