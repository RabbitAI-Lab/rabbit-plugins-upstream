## Description:

Helps generate a transition video between supplied first and last frames using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to request a transition video from first and last frame images and a text prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media supplied to the service may be uploaded for processing.

Mitigation: Submit only media approved for upload to dLazy.

Risk: Login may save an API key in the user's local configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: Running the skill relies on an external npm CLI and hosted API.

Mitigation: Review the pinned CLI package before installation and confirm the hosted service is acceptable for the task.

## Reference(s):

- [dLazy CLI project (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage (skill metadata)](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Video asset links]

**Output Format:** [Markdown guidance and JSON command responses with generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task ID or download the result to a local path.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
