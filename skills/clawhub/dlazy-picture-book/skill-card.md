## Description:

Creates a complete picture book from a theme by helping the agent write a paged story, generate style-consistent illustrations and matching background music with dLazy, and assemble a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, parents, educators, and developers use this skill to turn a story theme into a portable illustrated picture book with page text, generated images, optional background music, and an HTML reader.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses an external dLazy CLI and may persist a dLazy API key locally.

Mitigation: Review the CLI before installing, prefer npx or a project-local install, run in a restricted project folder, and use DLAZY_API_KEY for single-run authentication when local key storage is not desired.

Risk: Generated HTML has an injection risk if book.json content is not trusted.

Mitigation: Build books only from trusted book.json content, inspect generated HTML before sharing, and avoid hosting it on a trusted site until media paths are validated or safe DOM APIs are used.

Risk: Prompts, parameters, and local reference images may be sent to dLazy-hosted API and media endpoints.

Mitigation: Do not include sensitive personal, confidential, or regulated content in prompts or reference images unless that use is approved for the dLazy service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON book data, shell commands, generated media files, and HTML output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces book.json, image assets, background music, and index.html for a self-contained picture-book folder.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
