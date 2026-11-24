## Description:

Creates a picture book from a theme by writing a paged story, generating consistent illustrations and matching background music, and assembling the book as HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users ask an agent to turn a theme into a picture book, with a paged story, consistent illustrations, matching music, and a browsable HTML book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security analysis is partial, with unresolved references, and its guidance calls out an area in SKILL-cn.md for review.

Mitigation: Review the noted area and check that host file access permissions fit the intended use before running the skill.

Risk: Prompts and local reference images are sent to dLazy hosted services for generation.

Mitigation: Avoid using sensitive prompts or images unless their transfer to those services is appropriate.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Images, Audio]

**Output Format:** [Paged story data in book.json and an HTML picture book with image and audio assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; the output folder uses relative asset paths and can be shared or opened offline.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
