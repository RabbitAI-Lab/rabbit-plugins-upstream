## Description:

A structured skill for planning and generating platform-adapted social-media visuals and captions for Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and similar channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan social-media image concepts, platform-specific aspect ratios and safe areas, in-image copy, captions, and dLazy CLI generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and local media files provided for generation may be sent to dLazy hosted endpoints.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable, and avoid sending confidential media unless that use is approved.

Risk: An API key may be stored under the user's profile when CLI login or manual auth storage is used.

Mitigation: Use the DLAZY_API_KEY environment variable for ephemeral credentials when persistent local storage is not desired, and rotate or revoke keys through dLazy account controls when needed.

Risk: The artifact documentation contains inconsistent dLazy CLI version references.

Mitigation: Review the intended @dlazy/cli npm package version before installing or executing the CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs when execution is performed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform checks, layout plans, in-image text, captions, and next-step suggestions.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
