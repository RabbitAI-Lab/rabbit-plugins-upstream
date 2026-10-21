## Description:

Helps creators plan and generate platform-tailored social media visuals, in-image copy, and captions using the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and generate platform-specific social media images, carousel layouts, headlines, and captions for Instagram, TikTok, YouTube, LinkedIn, and Xiaohongshu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI sends prompts and parameters to dLazy and may upload local media supplied for generation.

Mitigation: Review the CLI package before installation and avoid sharing sensitive prompts or media without authorization.

Risk: A dLazy API key can be stored in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per run if persistent credentials are undesirable; restrict access to stored credentials.

Risk: The skill documentation contains mismatched version claims for the skill and CLI.

Mitigation: Check the actual release and CLI package versions before relying on installation instructions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source referenced by skill](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Image URLs]

**Output Format:** [Markdown with design plans, captions, commands, and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform format and safe-area checks, separate in-image text and captions, and iteration suggestions.]

## Skill Version(s):

1.3.33 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
