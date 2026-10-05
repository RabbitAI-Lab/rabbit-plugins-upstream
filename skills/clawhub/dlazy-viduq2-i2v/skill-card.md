## Description:

Turns still images into short videos with Vidu Q2 through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn reference images or first and last frames into short videos with optional audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied to the CLI may be uploaded to dLazy-hosted services.

Mitigation: Use only media you are authorized to share; avoid sensitive or regulated content unless the service terms and handling meet your needs.

Risk: Logging in may save an API key to local CLI configuration.

Mitigation: Protect local credentials, use a per-invocation environment variable when appropriate, and rotate or revoke keys if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text guidance and JSON CLI response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results can include hosted media URLs or an asynchronous task ID; generated media can optionally be saved locally.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; supplied skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
