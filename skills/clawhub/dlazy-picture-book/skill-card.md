## Description:

Creates a paged children's picture book from a theme, with consistent illustrations, background music, and a portable HTML reading experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and families use this skill to turn a theme into an illustrated, read-aloud children's story with optional background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy's hosted service.

Mitigation: Use the service only for material you are comfortable sharing with dLazy.

Risk: Authentication may store an API key locally on shared machines.

Mitigation: Prefer per-invocation environment credentials or npx on shared machines, and protect the key.

Risk: Illustration, music, and book files are downloaded and written locally.

Mitigation: Keep generated files in a dedicated output folder.

## Reference(s):

- [ClawHub picture-book skill](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Images, Audio, Shell commands]

**Output Format:** [Paged story and book.json, with an HTML book referencing PNG illustrations and MP3 music]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; generated files are kept together in a portable folder.]

## Skill Version(s):

1.3.25 (source: ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
