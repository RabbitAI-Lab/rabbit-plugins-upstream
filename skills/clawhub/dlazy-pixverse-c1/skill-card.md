## Description:

PixVerse C1 video generation skill for text-to-video, image-to-video, first/last-frame video, and reference-driven video workflows, with emphasis on action, VFX, and high-motion scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative automation users can use this skill to call the dLazy PixVerse C1 CLI for video generation from prompts, image references, first and last frames, or other supported media inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and local media paths supplied by the user may be sent to dLazy cloud endpoints.

Mitigation: Use the skill only for data suitable for the dLazy service and review media inputs before invoking generation.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use per-invocation DLAZY_API_KEY where persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Video generation may consume account credits.

Mitigation: Use dry-run or cost-estimation behavior when appropriate and confirm available credits before long or repeated generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, asynchronous task identifiers, status data, and error information from the dLazy CLI.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
