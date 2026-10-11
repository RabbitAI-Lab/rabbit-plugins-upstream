## Description:

Helps generate transition videos from a supplied first frame, last frame, and prompt using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide a video-generation request from first and last frame images and a text prompt through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy cloud services.

Mitigation: Share only media and prompt content approved for third-party processing.

Risk: Using the third-party CLI may install software globally or save an API key locally.

Mitigation: Review the package before installation; consider on-demand npx use and a per-invocation DLAZY_API_KEY.

Risk: Example flags and the sample image output conflict with the documented first/last-frame video workflow.

Mitigation: Check the CLI help and actual response before relying on the examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source (skill metadata link; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance with CLI commands and JSON result references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful requests can return a generated-asset URL; asynchronous requests return a task ID for later status checks.]

## Skill Version(s):

1.3.27 (source: ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
