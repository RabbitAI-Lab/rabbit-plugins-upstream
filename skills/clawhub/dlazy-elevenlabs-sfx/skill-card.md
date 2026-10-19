## Description:

Generates 1–22-second sound effects from text descriptions for foley, ambience, alerts, and games.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short sound effects from written prompts for media and games through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media can be sent to dLazy services; outputs are hosted by dLazy.

Mitigation: Avoid submitting sensitive material without approval and review dLazy's handling of uploaded media and generated outputs.

Risk: The third-party CLI requires an API key, which the login flow can store locally.

Mitigation: Review the CLI before installation and use per-invocation credentials or on-demand execution if local persistence is a concern.

Risk: The documented example labels a sound-effect result as a PNG image.

Mitigation: Treat the image example as a documentation error and verify the actual media type before using the result.

## Reference(s):

- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and links to generated sound effects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated sound effects can be returned as hosted links or downloaded locally.]

## Skill Version(s):

1.3.31 (source: server-resolved release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
