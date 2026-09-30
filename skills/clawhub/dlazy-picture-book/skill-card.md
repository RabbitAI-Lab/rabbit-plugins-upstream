## Description:

Creates a paged picture book from a theme, with a narrated story, consistent illustrations, background music, and a portable HTML reading experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, educators, and creators use this skill to turn a story idea into an illustrated children's book with optional background music and a browsable HTML edition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI sends prompts and reference images to dLazy services and requires an API key.

Mitigation: Review the CLI package before installation, use only images you are comfortable uploading, and use DLAZY_API_KEY for temporary access instead of saving a key.

Risk: Generated book files can overwrite existing files in the chosen output location.

Mitigation: Run the workflow in a dedicated output folder.

## Reference(s):

- [dLazy CLI repository (linked in package metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Files]

**Output Format:** [Paged story text and a portable HTML book with JSON content, PNG illustrations, and MP3 music]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; local media files are referenced by relative paths.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
