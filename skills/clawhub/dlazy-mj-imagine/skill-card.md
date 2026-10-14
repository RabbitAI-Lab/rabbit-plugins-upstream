## Description:

Helps generate stylized images from prompts with selectable aspect ratio, bot type, and grid or U1–U4 output through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request stylized image generation and select the aspect ratio, bot type, and grid or individual output position.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI may expose the user to unreviewed package behavior or service terms.

Mitigation: Review the pinned @dlazy/cli package and dLazy terms before use; use the on-demand npx option if a global installation is unwanted.

Risk: Prompts and any local files supplied to the CLI may be sent to dLazy's hosted service.

Mitigation: Avoid supplying private prompts or local files unless you intend to share them with the hosted service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image links]

**Output Format:** [Markdown instructions and JSON responses containing image URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can optionally be downloaded to a local path.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
