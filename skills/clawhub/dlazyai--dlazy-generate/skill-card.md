## Description:

A comprehensive generation skill. Can generate images, videos, and audio by automatically selecting the appropriate dlazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to route image, video, or audio generation requests to a suitable dlazy CLI model and receive generated media or result links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad generation triggers may activate the skill when a user did not intend to make an image, video, or audio request.

Mitigation: Invoke it for explicit media-generation requests and confirm the intended media type before running a model command.

Risk: Prompts and supplied local media are sent to dLazy hosted services, and returned media is hosted there.

Mitigation: Review prompts and input files for sensitive information before sending them to the hosted API, and review the skill instructions and referenced material before installation because the security analysis is partial.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-generate)

## Skill Output:

**Output Type(s):** [Images, Videos, Audio, JSON]

**Output Format:** [Generated media with a JSON result envelope and hosted media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model-dependent media outputs; dlazy CLI commands can be chained using pipe references.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
