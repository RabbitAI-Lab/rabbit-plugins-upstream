## Description:

Creates a picture book from a theme with a paged story, consistent illustrations, matching background music, and a portable HTML reader.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating children's picture books or bedtime stories can use the skill to turn a theme into a paged story with illustrations, background music, and a ready-to-open HTML book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local reference images are sent to dLazy hosted services for image and music generation.

Mitigation: Avoid including sensitive content in prompts or reference images, and review the service terms before sending material.

Risk: The CLI stores an API key in the user's local configuration file.

Mitigation: Protect access to the local account and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Images, Audio, HTML]

**Output Format:** [Paged story data and a portable HTML picture book with illustration and music assets]

**Output Parameters:** [Variable page count; defaults to 10 pages]

**Other Properties Related to Output:** [The book folder includes book.json, index.html, page images, and optional background music.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
