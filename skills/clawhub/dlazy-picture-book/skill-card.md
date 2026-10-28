## Description:

Creates a complete picture book from a theme by writing a paged story, generating consistent illustrations and matching background music, then assembling a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to turn a theme into a paged children's story with consistent illustrations and matching background music, then assemble it into a portable HTML picture book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy-hosted services, and generation uses account credits.

Mitigation: Use only prompts and images approved for that service, and check available credits before generating.

Risk: Crafted image paths in book data could inject active content into the generated HTML.

Mitigation: Use trusted book data with simple local media filenames, and assemble books in a dedicated output folder.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Images, Audio]

**Output Format:** [Paged story data (book.json) and a self-contained HTML picture book with image and music assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The finished book uses relative media paths and can be opened locally. Image and music generation use dLazy-hosted services.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
