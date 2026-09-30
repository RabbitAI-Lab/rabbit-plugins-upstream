## Description:

Helps agents synchronize a speaker's lip movements in a video to a supplied voice track, with an optional reference image to select a face.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to match a person's mouth movements in an existing video to new speech, optionally selecting the subject with a reference face image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use a scoped key, protect local configuration, and rotate or revoke the key if exposed.

Risk: Provided video, audio, and reference images may be uploaded to dLazy's hosted service.

Mitigation: Only submit media you are authorized to share and review the service terms before uploading sensitive content.

Risk: The sample output documentation appears inaccurate for a video-generation result.

Mitigation: Check actual CLI output and the generated asset type rather than relying on the sample response.

Risk: Using the skill installs or invokes a third-party CLI package.

Mitigation: Review the pinned CLI package and its source before installing if the publisher is not already trusted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with hosted result URLs, or an asynchronous task ID; it can save the result locally.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
