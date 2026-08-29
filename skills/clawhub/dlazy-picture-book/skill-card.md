## Description:

Creates a complete picture book from a theme by helping an agent draft a paged story, generate style-consistent illustrations with the dLazy CLI, generate matching background music, and assemble a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through creating a children's picture book or bedtime story package, including story text, generated illustrations, background music, and a portable HTML reading experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends prompts and any reference images to dLazy services for generation.

Mitigation: Use the skill only when third-party processing is acceptable, and avoid including sensitive prompts or images.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Prefer DLAZY_API_KEY for temporary authentication on shared machines, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill writes generated book files and media into the local filesystem.

Mitigation: Run it from a dedicated output folder and review generated files before sharing or publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, HTML, and bash command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides creation of book.json, index.html, image assets, and optional music assets in a local output folder.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
