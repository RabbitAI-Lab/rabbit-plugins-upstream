## Description:

Guides agents in planning Amazon product detail page imagery, including main images, secondary images, and A+ content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers and creative teams use this skill to plan and create Amazon product listing visuals, including compliant main images, supporting product imagery, and A+ brand content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reported an unexplained `dlazy login` command and unresolved local references, so installation and authentication behavior was only partially assessed.

Mitigation: Review the CLI installation and authentication requirements, and proceed only if they are understood and accepted.

Risk: The skill describes uploading supplied local media to dLazy-hosted storage for processing.

Mitigation: Avoid sending confidential or personal media unless its transfer to the hosted service is approved.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Generated image assets with Markdown planning and progress summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image scope varies by request; rendering uses the dLazy hosted service.]

## Skill Version(s):

1.3.39 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
