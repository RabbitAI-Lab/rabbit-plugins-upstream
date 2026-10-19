## Description:

Helps agents generate short videos with MiniMax Hailuo from text, start and end frames, or reference media through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, frame transitions, or reference images, videos, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI executes code outside this skill's files.

Mitigation: Review the package before installation and use its pinned npx version if a global installation is not desired.

Risk: Prompts and selected local media are sent to dLazy's hosted service; an API key is stored locally when using CLI login.

Mitigation: Only submit media approved for upload, protect the API key, and rotate or revoke it in the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted result URLs or an asynchronous task ID; generated assets can be saved locally.]

## Skill Version(s):

1.2.28 (source: ClawHub release; skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
