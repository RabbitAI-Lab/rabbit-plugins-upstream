## Description:

Selects dLazy CLI models to generate images, video, and audio from user requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run dLazy models for image, video, and audio generation or editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media may be sent to dLazy's cloud service, and generated outputs are hosted there.

Mitigation: Avoid sensitive prompts and local files unless you intend to share them with dLazy.

Risk: Logging in can save an API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for temporary sessions if you do not want a saved key.

Risk: Generation may consume account credits.

Mitigation: Check account credits and expected usage before running generation commands.

## Reference(s):

- [dLazy CLI project (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Command guidance and CLI JSON responses containing generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image, video, or audio generation may consume dLazy account credits.]

## Skill Version(s):

1.3.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
