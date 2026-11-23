## Description:

Guides agents through adapting web novels into webtoon plot breakdowns, episode tags, and per-episode scripts, with an optional dLazy CLI image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the agent to turn web-novel chapters into structured plot breakdowns, episode tags, and visual, cliffhanger-driven webtoon scripts. It can also guide single-image generation through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The available security scan says CLI authentication, credential storage, local media access, and uploads are not fully clear.

Mitigation: Review the CLI's purpose, credential handling, and media upload behavior before installation or use; only provide local media intended for upload.

Risk: The security scan was partial because referenced files or paths were missing.

Mitigation: Review and scan the complete referenced CLI files and paths before relying on the skill.

## Reference(s):

- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Chinese Markdown with structured plot breakdowns, episode scripts, and occasional CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversation-based; adaptation content follows the supplied novel and revision notes.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
