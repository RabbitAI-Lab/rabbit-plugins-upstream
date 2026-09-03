## Description:

Creates a complete picture book from a theme by helping the agent write a paged story, generate consistent illustrations with dLazy image generation, generate matching background music, and assemble a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create illustrated children's picture books or bedtime storybooks as portable HTML projects with page text, generated images, and background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and reference images to dLazy hosted services.

Mitigation: Use it only with content that may be processed by dLazy, and avoid submitting sensitive prompts or reference images unless the user accepts that service use.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied by environment variable.

Mitigation: Store the key using the dLazy CLI's authentication flow or a scoped environment variable, and rotate or revoke it if exposure is suspected.

Risk: Generated book files are written into the working directory and could overwrite unrelated files if names collide.

Mitigation: Run the skill in a fresh project folder and review generated paths before assembling the final HTML.

Risk: Image and music generation can consume dLazy credits.

Mitigation: Confirm the intended page count and generation settings before running the dLazy commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON book data, generated media files, and a self-contained HTML book]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, python3, curl, a dLazy API key, hosted dLazy generation APIs, and local output files.]

## Skill Version(s):

1.3.11 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
