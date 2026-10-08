## Description:

Checks images, videos, and audio for signs of AI generation, reporting confidence scores, possible deepfakes, and likely generators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams checking whether an image, video, or audio clip may be AI-generated use this skill to obtain confidence scores, deepfake indicators, and possible generator attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio can be uploaded to dLazy's hosted service without a prominent consent step.

Mitigation: Confirm the specific media before analysis; avoid sensitive files unless the service's privacy and retention terms are acceptable.

Risk: The login flow saves an API key in local CLI configuration.

Mitigation: Use a per-task API key when a saved credential is not desired, and protect any locally stored key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and summarized JSON detection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include confidence scores and likely generator; asynchronous requests return a task ID.]

## Skill Version(s):

1.0.25 (source: release metadata; skill frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
