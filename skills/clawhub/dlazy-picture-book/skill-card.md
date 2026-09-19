## Description:

Creates complete picture books from a theme by drafting the paged story, generating style-consistent illustrations and background music with dLazy services, and assembling a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create a children's picture book or bedtime story from a brief, including story text, generated illustrations, background music, and a portable HTML reading experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to the third-party dLazy API and media storage.

Mitigation: Use non-sensitive prompts and reference images, and review dLazy's service terms before submitting private or regulated content.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: On shared or sensitive machines, prefer the DLAZY_API_KEY environment variable over saved credentials and rotate or revoke keys if exposure is suspected.

Risk: The workflow creates local book output files and downloads generated media into project folders.

Mitigation: Run the skill in a dedicated project directory and review output paths before downloading media or building the final HTML.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands, generated JSON data, and local HTML/media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local picture-book folder containing index.html, book.json, images, and optional background music; media generation depends on the third-party dLazy CLI/API.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
