## Description:

Helps turn a webpage URL into a promotional, social-ad, or product-demo video through the dLazy website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to request a promotional, social-ad, or product-demo video from a webpage URL and continue working on the resulting project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and URLs are sent to dLazy, and files attached with --files may be uploaded to its service.

Mitigation: Use this workflow only if comfortable sharing the inputs with dLazy; attach only files intended for upload.

Risk: Logging in stores a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text with CLI commands and project responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation is requested through the dLazy service; the skill itself does not return a video file.]

## Skill Version(s):

1.0.24 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
