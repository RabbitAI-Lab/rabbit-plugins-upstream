## Description:

Helps agents generate videos with Tongyi Wanxiang 2.7 from text prompts, frame images, or reference media through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text, first and last frames, or reference images and videos, then receive links to generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running a third-party CLI executes code outside the skill itself.

Mitigation: Review the CLI before installation and use the pinned on-demand package if a persistent global installation is unwanted.

Risk: Prompts and selected media are sent to dLazy's hosted service.

Mitigation: Submit only prompts and media you are comfortable sharing with that service.

Risk: Signing in saves the API key in a local configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable when you do not want the key saved locally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Video links]

**Output Format:** [Text guidance and JSON responses with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of a completed media URL.]

## Skill Version(s):

1.3.27 (source: ClawHub release; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
