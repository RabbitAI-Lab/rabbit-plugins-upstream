## Description:

Creates illustrated picture books from a theme, with a paged story, consistent images, background music, and a browsable HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, families, and creators use this skill to turn a theme into a children's picture book with story text, illustrations, music, and an HTML reading experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to third-party dLazy services.

Mitigation: Use only content you are comfortable sharing with dLazy; avoid sensitive images and prompts.

Risk: Image and music generation uses dLazy API credits and may require a locally stored API key.

Mitigation: Confirm expected credit use, protect the key, and revoke or rotate it in the dLazy dashboard if needed.

Risk: The skill installs or runs a third-party CLI and downloads book assets into an output folder.

Mitigation: Review the CLI and the chosen output path; use the documented npx option to avoid a global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration guidance]

**Output Format:** [JSON story data and HTML picture book with local image and audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Portable book folder with relative image and music paths; 10 pages by default.]

## Skill Version(s):

1.3.27 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
