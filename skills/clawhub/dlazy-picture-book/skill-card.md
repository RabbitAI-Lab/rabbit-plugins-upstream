## Description:

Creates a complete picture book from a theme by guiding story planning, page-by-page illustration generation, background music generation, and local assembly into a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through producing a children's picture book from a theme, including paged story text, style-consistent generated illustrations, background music, and a shareable HTML reading experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs the external dLazy CLI and sends generation requests to hosted dLazy services.

Mitigation: Review the referenced npm package and source before installation, install only when the hosted service is intended, and avoid running the CLI with administrator privileges.

Risk: The workflow stores or uses a dLazy API key for hosted image and music generation.

Mitigation: Prefer per-invocation credentials where practical, keep the local CLI config restricted to the current OS user, and rotate or revoke the API key if exposure is suspected.

Risk: The generated HTML has an injection risk for untrusted media paths in book.json.

Mitigation: Use a dedicated output folder and do not build or open books from untrusted book.json files until the HTML escaping issue is fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands, JSON book data, local media files, and a generated HTML book]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical output folder contains book.json, index.html, generated images, and background music; hosted dLazy services are used for image and music generation.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
