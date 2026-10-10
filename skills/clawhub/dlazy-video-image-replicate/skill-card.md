## Description:

Studies a reference image or video and helps recreate its look and structure using the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use a reference image or video to request a similar composition or visual style featuring their own product, subject, or characters through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached media are sent to the dLazy service, including uploaded local files.

Mitigation: Avoid attaching confidential files unless dLazy's terms and your organization's policy permit it.

Risk: The CLI stores an API key locally when used with persistent authentication.

Mitigation: Protect local credentials and use a per-invocation API key when persistent storage is undesirable.

Risk: Selecting the wrong existing project may expose context from earlier work.

Mitigation: Confirm the project ID before continuing an existing project.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streamed text response from the dLazy agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped conversation; reference files can be supplied as inputs.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release; skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
