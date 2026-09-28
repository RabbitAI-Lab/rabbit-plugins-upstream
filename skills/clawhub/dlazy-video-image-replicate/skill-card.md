## Description:

Recreates the look and structure of a reference image or video using the user's own subject, product, or characters through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to recreate the style and structure of a reference image or video with their own subjects, products, or characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached reference media are sent to dLazy's hosted service.

Mitigation: Avoid attaching sensitive files unless you intend to upload them, and use the service only if its data handling is acceptable.

Risk: An API key may be stored in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: Selecting a previous project may reuse earlier conversation context.

Mitigation: Check the project ID before continuing a task and start a new project when prior context should not be reused.

Risk: The skill invokes a third-party CLI package.

Mitigation: Review the pinned CLI package and declared source before installing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Images, Video]

**Output Format:** [Conversational text and generated image or video deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Follow-up conversations can reuse context from a selected project.]

## Skill Version(s):

1.3.22 (source: server-resolved ClawHub release; supplied skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
