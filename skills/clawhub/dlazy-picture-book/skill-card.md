## Description:

Creates a complete picture book from a theme by helping an agent write a paged story, generate style-consistent illustrations and background music with dLazy services, and assemble a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create children's picture books, storybooks, illustrated bedtime stories, and portable HTML reading experiences from a theme or short creative brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to dLazy services, and local reference images may be uploaded to dLazy media storage.

Mitigation: Avoid using sensitive local images or confidential story material as inputs unless the user is comfortable sending them to dLazy services.

Risk: The dLazy API key may be stored in the user's CLI configuration.

Mitigation: Use per-invocation credentials when appropriate, and rotate or remove stored keys when access is no longer needed.

Risk: The workflow depends on npm or npx, python3, curl, and generated media downloads.

Mitigation: Run commands one at a time in a controlled project folder and review downloaded result URLs before assembling the final HTML book.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and generated HTML book assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent typically produces book.json, image and music download commands, and an index.html assembled from local template assets.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
