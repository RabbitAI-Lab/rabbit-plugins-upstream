## Description:

Creates a complete picture book from a theme by drafting a paged story, generating style-consistent illustrations with dlazy gpt-image-2, generating background music with dlazy elevenlabs-music, and assembling a portable HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn a picture-book idea into a complete illustrated story package with paged text, generated images, background music, and an HTML reading experience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Story prompts and reference images are sent to dLazy services and reference images may be uploaded to dLazy media storage.

Mitigation: Use only when comfortable sharing that content with dLazy; avoid sensitive prompts or images and rotate or revoke the local API key if exposed.

Risk: Crafted book.json content can inject script into the generated HTML.

Mitigation: Use trusted book.json content, review generated index.html before hosting or sharing, and constrain execution until template escaping or DOM construction is hardened.

Risk: The workflow depends on a third-party CLI/API and a locally stored dLazy API key.

Mitigation: Review the npm package or source before installation, prefer a constrained workspace, and keep API key storage restricted to the intended user account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands, JSON book data, and HTML/CSS/JavaScript output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local book folder containing index.html, book.json, images, and optional background music.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
