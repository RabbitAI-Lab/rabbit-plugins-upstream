## Description:

Creates an illustrated, narrated picture book from a theme, with a paged story, consistent artwork, background music, and a browsable HTML edition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and families use this skill to turn a story theme into a children's picture book with page-by-page illustrations, music, and an offline-readable HTML edition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation may incur paid dLazy usage and send story prompts and reference images to hosted services.

Mitigation: Confirm costs and avoid uploading sensitive material before generating the book.

Risk: The dLazy API key may persist in the local user configuration, which is unsuitable for shared machines.

Mitigation: Use per-invocation credentials or avoid saving a key on shared devices; rotate or revoke exposed keys.

Risk: The workflow downloads media and writes a local book folder.

Mitigation: Review the CLI package before installation and confirm output paths and downloaded media before sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (tooling, not verified skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Shell commands]

**Output Format:** [Paged story text, book.json, and an HTML book with referenced image and audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; the book folder can be opened locally with its media files.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
