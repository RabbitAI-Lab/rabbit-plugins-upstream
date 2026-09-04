## Description:

Creates a complete picture book from a theme by helping an agent write a paged story, generate consistent page illustrations with dLazy image generation, generate background music, and assemble a portable HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create children's picture books, storybooks, illustrated bedtime stories, or similar paged narratives with matching visuals, music, and a self-contained HTML reading experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and reference images to dLazy services for generation.

Mitigation: Use only prompts and images that are appropriate to share with dLazy services, and review inputs before generation.

Risk: Authentication may store a dLazy API key in a local CLI configuration file.

Mitigation: Use DLAZY_API_KEY or npx for less persistent setup when appropriate, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: Image and music generation can spend dLazy credits.

Mitigation: Confirm the account and budget before generation, and generate assets sequentially so cost and quality can be reviewed page by page.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON data examples and shell commands that produce local book files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent workflow produces book.json, generated image and music assets, and a self-contained index.html picture book.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
