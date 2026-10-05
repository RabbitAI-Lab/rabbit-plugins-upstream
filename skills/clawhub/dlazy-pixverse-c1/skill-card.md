## Description:

Helps agents generate PixVerse C1 videos from text, images, first and last frames, or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, images, or reference frames and receive links to generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy, and generated media is hosted by dLazy.

Mitigation: Review content before sending it and avoid uploading sensitive media without authorization.

Risk: Signing in may save a dLazy API key on the local device.

Mitigation: Protect local credentials and revoke the key through the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include hosted media links or an asynchronous task ID; media can optionally be downloaded locally.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
