## Description:

Guides an agent in generating stylized images through dLazy's Midjourney-style service, with aspect ratio, bot type, and grid or U1–U4 output choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request stylized images with chosen aspect ratios, bot types, and grid or selected image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any selected local media are sent to the dLazy service.

Mitigation: Only submit content you are authorized to share with dLazy.

Risk: Using the skill requires trusting the external dLazy CLI package and service.

Mitigation: Review the CLI and service before installation or use.

Risk: The CLI can persist an API key on the local device.

Mitigation: Use a per-invocation DLAZY_API_KEY when local persistence is unwanted; rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance and CLI JSON results containing image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be downloaded locally; asynchronous requests return a task ID instead of immediate outputs.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
