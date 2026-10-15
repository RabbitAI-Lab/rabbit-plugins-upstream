## Description:

Creates a paged children's picture book with a written story, consistent illustrations, background music, and a browsable HTML edition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and families use this skill to turn a theme into a children's storybook with illustrated pages and background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required external dLazy CLI is not included with the skill.

Mitigation: Review the CLI package before installing or running it.

Risk: Prompts and reference images are sent to dLazy hosted services; generated media is hosted there too.

Mitigation: Avoid sharing sensitive content and confirm that uploaded images are suitable for the service.

Risk: CLI login can save the API key in a local configuration file.

Mitigation: Use DLAZY_API_KEY for per-session authentication if persistent storage is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source (external dependency, not skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Guidance]

**Output Format:** [Paged story JSON and an HTML picture book with illustrations and background music]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; the book folder includes locally referenced images and music.]

## Skill Version(s):

1.3.28 (ClawHub release; bundled skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
