## Description:

Creates illustrated picture books from a theme by writing a paged story, generating coordinated illustrations and background music through dLazy, and assembling an HTML reading experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and families use this skill to turn a theme into a paged children's story with consistent illustrations, background music, and a locally viewable picture book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Story prompts and reference images are sent to a third-party service.

Mitigation: Confirm before sending content and avoid sharing sensitive prompts or images.

Risk: A dLazy API key is required and may be stored locally.

Mitigation: Protect the key, and prefer DLAZY_API_KEY on shared machines.

Risk: Image and music generation may consume account credits.

Mitigation: Confirm the planned generation scope with the user before running it.

## Reference(s):

- [Picture Book skill on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files]

**Output Format:** [JSON story data, HTML, PNG illustrations, and MP3 audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; the HTML references local images and music by relative path.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
