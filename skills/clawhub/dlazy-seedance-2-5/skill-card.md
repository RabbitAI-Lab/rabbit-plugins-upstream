## Description:

Guides agents through generating Seedance 2.5 videos with the dLazy CLI, including reference media and first/last-frame controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation through dLazy, with prompts, reference media, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running a third-party npm CLI executes code outside the skill text.

Mitigation: Review the CLI before installing; use the documented on-demand npx invocation instead of a persistent global install if preferred.

Risk: Prompts and explicitly supplied media are sent to dLazy's cloud service.

Mitigation: Do not submit private prompts or media unless you are comfortable uploading them to that service.

Risk: Logging in may save a dLazy API key locally.

Mitigation: Use the DLAZY_API_KEY environment variable when a saved local key is not desired.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return hosted output URLs or an asynchronous task ID; skill metadata pins CLI version 1.2.3.]

## Skill Version(s):

1.2.25 (source: ClawHub release metadata; bundled skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
