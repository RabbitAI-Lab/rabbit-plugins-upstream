## Description:

Creates a complete picture book from a theme by writing a paged story, generating style-consistent illustrations and background music through the dLazy CLI, and assembling a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a picture-book theme into a portable HTML storybook with generated illustrations, story text, and background music. It is suited to children's books, illustrated stories, and bedtime story workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends prompts, reference images, and generated media requests through third-party dLazy services.

Mitigation: Use the skill only when that data flow is acceptable, avoid sensitive inputs, and review dLazy account and service terms before use.

Risk: API keys may be saved in the local dLazy CLI configuration on shared machines.

Mitigation: Prefer DLAZY_API_KEY for per-invocation use on shared systems and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The workflow installs or runs a third-party CLI and downloads generated media with curl.

Mitigation: Review the referenced dLazy CLI package before installation and keep generated output in a dedicated project folder.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and shell commands; the workflow produces book.json, generated media files, and index.html.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, python3, curl, and dLazy API credentials; generated prompts, reference images, and media requests are sent to dLazy services.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
