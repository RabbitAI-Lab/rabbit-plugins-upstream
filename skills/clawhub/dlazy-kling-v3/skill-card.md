## Description:

Powerful video generation with Kling v3 for high-quality text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to invoke the dLazy hosted Kling v3 service for text-to-video or image-to-video generation from prompts and optional media references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and media files may be sent to dLazy hosted services.

Mitigation: Use the skill only with content approved for dLazy processing and run dry-run or npx first when reviewing payloads, persistence, or cost.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Use an organization API key that can be rotated or revoked, or provide DLAZY_API_KEY per invocation when persistent local storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source link from metadata](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance]

**Output Format:** [JSON CLI responses with generated media URLs or async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return files.dlazy.com output URLs or a generateId for asynchronous polling.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
