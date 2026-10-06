## Description:

Creates illustrated picture books from a theme, pairing a paged story with consistent images and background music in a locally viewable HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, parents, educators, and creators use this skill to turn a story theme into a children's picture book with page-by-page illustrations and background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI and supplying a dLazy API key exposes credentials to that service.

Mitigation: Review the CLI before installation and confirm the user is comfortable saving or supplying a dLazy API key.

Risk: Image and music generation sends prompts and any reference images to hosted dLazy services and consumes credits.

Mitigation: Get explicit confirmation before generating, and avoid sending reference images the user does not want uploaded.

Risk: The workflow creates a local folder containing story JSON, HTML, illustrations, and music.

Mitigation: Confirm the intended output location before creating files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, HTML, JSON, Images, Audio]

**Output Format:** [Local picture-book folder with index.html, book.json, illustrations, and background music]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [HTML references images and music by relative paths; the complete folder can be opened locally.]

## Skill Version(s):

1.3.24 (source: ClawHub release evidence; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
