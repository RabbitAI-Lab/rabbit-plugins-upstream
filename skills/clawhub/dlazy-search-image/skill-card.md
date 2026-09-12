## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and developers use this skill to search for image references, backgrounds, and design assets by keyword through the dLazy CLI. It is best treated as a dLazy cloud CLI integration rather than a direct Pixabay-only search tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill is a dLazy cloud CLI wrapper while it is presented as a Pixabay keyword image search tool.

Mitigation: Review data flows before installation and treat invocations as calls to dLazy cloud services.

Risk: Local file paths passed to media fields may be uploaded to dLazy media storage.

Mitigation: Do not pass local file paths unless the user intends those files to be uploaded.

Risk: The skill can use a global npm install and persistent API key configuration.

Mitigation: Prefer on-demand execution or review the dLazy CLI package and account workflow before global installation or storing an API key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON results with image URLs and metadata, plus concise CLI guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; results may include hosted asset URLs and optional saved files when a save path is provided.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
