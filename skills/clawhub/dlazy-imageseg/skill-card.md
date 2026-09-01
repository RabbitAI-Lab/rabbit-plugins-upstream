## Description:

Separates foreground subjects from image backgrounds and returns a transparent-background image URL for product images, people cutouts, and compositing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted image matting service from an agent workflow, producing transparent-background image assets from image URLs or local image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided image files are uploaded to dLazy's hosted service for processing.

Mitigation: Do not pass private or sensitive images unless upload to dLazy is intended.

Risk: The CLI can store an API key in a local user configuration file after login.

Mitigation: Use DLAZY_API_KEY per invocation when a persistent local credential is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing generated image output URLs, or an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
