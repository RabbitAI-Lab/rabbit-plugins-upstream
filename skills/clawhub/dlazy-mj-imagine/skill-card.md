## Description:

Helps agents generate stylized images through dLazy using prompts, aspect ratios, bot types, and grid or U1–U4 output selections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request stylized images from dLazy and select an aspect ratio, bot type, and output position.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local files may be sent to dLazy, and generated assets are hosted by dLazy.

Mitigation: Review prompts and file paths before submission; avoid sharing sensitive content.

Risk: Login stores an API key locally.

Mitigation: Protect the local credential and rotate or revoke it in the dLazy dashboard if needed.

Risk: A global CLI installation persists on the system.

Mitigation: Use the pinned on-demand npx command if a persistent installation is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted image URLs or asynchronous task status; images can optionally be saved locally.]

## Skill Version(s):

1.3.22 (source: server-resolved release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
