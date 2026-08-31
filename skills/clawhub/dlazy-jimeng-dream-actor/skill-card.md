## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Jimeng Dream Actor CLI for cloud-hosted image-to-video generation from a prompt and a reference character image or video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be sent to dLazy's cloud service for processing.

Mitigation: Confirm the user intends to use dLazy before sending generic image-to-video requests, and avoid submitting sensitive prompts or media unless cloud processing is acceptable.

Risk: Local image, video, or audio paths supplied to the CLI may be uploaded to dLazy-hosted media storage.

Mitigation: Review local file paths before invocation and use only files the user has approved for upload.

Risk: Authentication may store a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation environment keys when persistent credentials are not desired, and rotate or revoke stored keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, dLazy API authentication, and network access to dLazy API and file hosting endpoints.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
