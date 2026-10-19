## Description:

Helps agents generate or edit images with Vidu Q2 through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate images from prompts or edit images using supplied references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Send only content approved for the hosted service and review generated links before sharing.

Risk: Login may save an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be returned as hosted URLs or saved locally.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
