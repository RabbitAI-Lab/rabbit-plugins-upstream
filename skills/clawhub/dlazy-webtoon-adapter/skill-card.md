## Description:

This skill guides Chinese-language web-novel adaptation into webtoon dramas, including genre selection, plot breakdown, episode tagging, and per-episode script writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to turn web-novel material into webtoon-ready breakdowns, episode tags, and per-episode scripts. It also guides optional dLazy CLI use for authenticated generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send prompts and user-selected media files to dLazy SaaS endpoints.

Mitigation: Confirm the material is appropriate for external processing before generation or upload, and require explicit user confirmation for each upload or generation step.

Risk: Authentication may store a dLazy API key in a local CLI configuration file.

Mitigation: Prefer per-command environment-variable authentication when practical, restrict local credential access, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill may install or run an npm CLI before invoking hosted generation services.

Mitigation: Review the pinned CLI version and source before use, prefer pinned npx execution for temporary use, and install only in environments approved for external SaaS workflows.

Risk: Terminal execution instructions are broad relative to the writing workflow.

Mitigation: Keep command execution limited to reviewed dLazy CLI commands and require explicit confirmation before each generation command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown conversation responses with optional inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language adaptation output; optional dLazy CLI actions require authentication and explicit user confirmation.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
