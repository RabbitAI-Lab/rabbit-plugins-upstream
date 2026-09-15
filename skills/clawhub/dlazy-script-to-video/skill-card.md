## Description:

Turns a script, screenplay, or shot list into a storyboarded, shot-by-shot video workflow using the pinned dLazy storyboard CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill when a user provides a script or scene breakdown and wants a multi-shot storyboarded video workflow with consistent characters, shot prompts, generated media, and assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected files, and project context may be sent to dLazy services, and attached files may be uploaded.

Mitigation: Use the skill only when this SaaS data handling is acceptable, and avoid sending sensitive files unless authorized.

Risk: The skill relies on a pinned third-party npm CLI and a dLazy API key.

Mitigation: Prefer on-demand npx use when a persistent binary is unnecessary, avoid administrator-level npm installs, and use a revocable API key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI response text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; attached files may be uploaded through the dLazy CLI for project-scoped sessions.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
