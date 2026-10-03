## Description:

Creates an illustrated picture book from a theme, pairing a paged story with consistent images and background music in a locally assembled HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and other external users can turn a theme into a children's picture book with short page-by-page text, illustrations, and background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to third-party dLazy services.

Mitigation: Avoid private reference images unless you intend to upload them, and review content before sending.

Risk: The dLazy CLI uses an API key stored locally.

Mitigation: Keep the key private and use a dedicated output folder for generated files.

## Reference(s):

- [ClawHub picture-book release](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source (tool dependency)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Files, Images, Audio]

**Output Format:** [JSON story and HTML book with local PNG illustrations and MP3 music]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; HTML references media using relative paths.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
