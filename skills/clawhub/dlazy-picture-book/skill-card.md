## Description:

Creates a complete picture book from a theme by helping an agent write a paged story, generate style-consistent illustrations and background music with dLazy services, and assemble a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, educators, and developers use this skill to produce portable HTML picture books from a story theme, including page text, illustrations, background music, and assembled files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference images may be sent to dLazy services for image and music generation.

Mitigation: Use the skill only with content appropriate for dLazy processing, and avoid submitting sensitive or private images unless that use is permitted.

Risk: A dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Use OS-protected local configuration, prefer a dedicated key where possible, and rotate or revoke the key if the machine is shared or compromised.

Risk: The HTML builder consumes book.json and writes a local output file.

Mitigation: Use a dedicated output folder and avoid building from untrusted book.json files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands plus JSON, HTML, image, and audio file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, python3, curl, and a dLazy API key; generated media and HTML are saved in a local book folder.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
