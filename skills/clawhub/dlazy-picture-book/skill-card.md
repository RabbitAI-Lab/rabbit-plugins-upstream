## Description:

Creates a picture book from a theme with a paged story, style-consistent illustrations, matching background music, and a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and creators use this skill to turn a picture-book theme into a paged story, coordinated illustrations and music, and a portable HTML book for reading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented image and music workflow sends prompts to dLazy services and may upload local reference images.

Mitigation: Avoid sending sensitive text or images, and review the service terms and tool permissions before use.

Risk: The security review was partial because some referenced paths were missing, so those references were not fully assessed.

Mitigation: Review the actual tool permissions and inspect missing or downloaded files before use.

## Reference(s):

- [dLazy CLI source (linked by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Images, Audio, HTML files, Guidance]

**Output Format:** [Paged story text, illustration and music files, and a self-contained HTML book]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; page count and story brief can be customized.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
