## Description:

A structured workflow skill dedicated to social-media carousel design, using a decide-intent-first approach with a single confirmation and cover-first workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and social media teams use the skill to plan carousel narratives, define slide roles and headlines, and guide cover-first image generation with dLazy. It helps structure the design direction and generation workflow for platforms such as Instagram, TikTok, Xiaohongshu, and LinkedIn.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy hosted services for processing.

Mitigation: Use only prompts and media you are comfortable sending to dLazy, and review generation requests before running them.

Risk: The documentation contains an outdated CLI version reference alongside the declared 1.2.3 installation pin.

Mitigation: Use the declared 1.2.3 install command and verify the package version before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [CLI project information (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured design guidance, Shell commands]

**Output Format:** [Markdown slide plans and guidance, with CLI setup and generation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow can invoke dLazy image generation; the CLI returns generated image URLs.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
