## Description:

Generates conversion-focused ecommerce advertising videos from product photos, links, specifications, or catalogs through dLazy's hosted agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and marketing teams use this skill to turn product materials into shopping and advertising videos for online stores and social commerce. It supports project-based follow-up and can generate videos with multilingual voiceover or an optional virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached product materials are uploaded to dLazy media storage and prompts are sent to its hosted service.

Mitigation: Upload only materials approved for sharing with dLazy and select the intended organization project.

Risk: The organization API key is saved in the local CLI configuration, and the external CLI and hosted service were not independently audited in this artifact review.

Mitigation: Protect access to the saved configuration, rotate or revoke the key when needed, and assess the CLI and service before using sensitive materials.

Risk: Video generation consumes organization credits.

Mitigation: Check available credits and expected usage before starting generation.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Generated ecommerce advertising video with streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multilingual voiceover and an optional virtual host. Attached local files are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.31 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
