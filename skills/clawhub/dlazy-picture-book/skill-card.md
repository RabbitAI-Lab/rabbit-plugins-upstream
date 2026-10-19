## Description:

Creates illustrated picture books from a theme, with a paged story, consistent artwork, background music, and a browsable HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and families use this skill to turn a story theme into a children's picture book with illustrated pages and background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted generation may consume dLazy credits.

Mitigation: Confirm expected credit usage before running image and music generation.

Risk: Prompts and reference images are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive text or images unless sharing them with dLazy is acceptable.

Risk: Authentication stores an API key in the local dLazy CLI configuration.

Mitigation: Protect the local account and rotate the key if it is exposed.

Risk: Generated book files are written into the working directory.

Mitigation: Use a dedicated output folder for each book.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI repository (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Story text and a folder containing HTML, JSON, PNG images, and MP3 audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A portable picture book with page navigation and optional background music.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
