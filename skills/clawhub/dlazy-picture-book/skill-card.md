## Description:

Creates an illustrated picture book from a theme, with a paged story, consistent artwork, background music, and a locally assembled HTML reader.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating children's stories use this skill to turn a theme into a paged picture book with illustrations and background music that can be opened locally in a browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Story prompts and reference images are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive material and use the service only when its data handling is acceptable.

Risk: Authentication can save an API key in local configuration.

Mitigation: On shared systems, prefer a per-invocation DLAZY_API_KEY and protect or revoke stored credentials.

Risk: The workflow installs and runs a third-party CLI and writes book assets locally.

Mitigation: Review the pinned CLI source and package before use, and keep outputs in a dedicated folder.

## Reference(s):

- [ClawHub picture-book skill](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files]

**Output Format:** [Paged story JSON, locally assembled HTML, illustration images, and background-music audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; HTML references local images and audio by relative paths.]

## Skill Version(s):

1.3.29 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
