## Description:

Creates motion graphics, kinetic typography, animated text videos, animated infographics, and explainer animations as code-driven Remotion-style graphics rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask the dLazy motion-graphics assistant to produce code-driven animated graphics, kinetic typography, animated infographics, explainer animations, and related project guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party SaaS CLI and requires a dLazy API key.

Mitigation: Use the on-demand npx invocation when possible, store keys only in the intended user account, and revoke or rotate keys from the dLazy dashboard when access should change.

Risk: Files attached with the CLI can be uploaded to dLazy-hosted storage.

Mitigation: Attach only files intended for the dLazy service and avoid including confidential or regulated data unless the service terms and organizational policy allow it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented guidance with inline shell commands and generated project instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes a pinned third-party CLI that can stream hosted-agent responses and continue project-scoped sessions.]

## Skill Version(s):

1.3.10 (source: ClawHub release metadata; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
