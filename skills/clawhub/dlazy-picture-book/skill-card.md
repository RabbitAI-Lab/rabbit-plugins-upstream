## Description:

Creates a paged picture-book story with consistent illustrations and background music, then assembles an HTML book for reading locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and families use this skill to turn a theme into an illustrated children's storybook with optional background music and a locally readable HTML presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs and runs a third-party CLI.

Mitigation: Review the CLI and install it only if you trust its publisher.

Risk: Prompts and reference images are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive stories or images unless you are comfortable sharing them with dLazy.

Risk: The workflow uses a dLazy API key and can spend dLazy credits.

Mitigation: Use DLAZY_API_KEY on shared machines, check available credits before generating, and work in a dedicated output folder.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy CLI source (not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Guidance]

**Output Format:** [Paged story data in JSON and a local HTML picture book with linked illustrations and audio.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 pages; keep the HTML, image files, and music file together for playback.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
