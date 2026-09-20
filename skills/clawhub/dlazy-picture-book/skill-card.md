## Description:

Creates complete picture books from a theme by drafting a paged story, generating style-consistent illustrations and background music through the dLazy CLI, and assembling a portable HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create illustrated children's picture books or bedtime storybooks from a theme. It guides story planning, dLazy-backed image and music generation, and local HTML assembly into a shareable book folder.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key that may be saved locally or supplied through the environment.

Mitigation: Use the documented dLazy login or auth flow, protect the local CLI configuration file, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Picture-book generation can spend dLazy credits through image and music API calls.

Mitigation: Confirm the intended page count, quality settings, and music duration before generation, and monitor credit usage before running a full book.

Risk: Prompts and local reference images are sent to dLazy-hosted services for media generation.

Mitigation: Avoid submitting sensitive prompts or private reference images unless the user accepts upload to dLazy API and media storage endpoints.

Risk: The final HTML book depends on local book.json, image, and music paths being consistent.

Mitigation: Keep index.html next to the generated images and music folders, and verify book.json paths before sharing the finished folder.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with JSON book data, shell commands, and generated HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a book.json plan, image and music asset paths, and an index.html picture-book build.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
