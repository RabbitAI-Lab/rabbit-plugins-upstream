## Description:

Generates realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and content creators use this skill to have an agent invoke the pinned dLazy CLI for digital human presenter video generation from a portrait image plus audio or text prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image or audio files are sent to dLazy-hosted API and media endpoints.

Mitigation: Review data sensitivity and service terms before use, and avoid sending confidential or regulated media unless approved for the hosted service.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through the environment.

Mitigation: Use OS-user-restricted configuration or per-invocation environment variables as appropriate, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Using a global npm install persists a third-party CLI on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI is preferred, and review the dLazy CLI source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI command examples and JSON result envelopes containing generated asset URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload selected image or audio inputs to dLazy-hosted endpoints; generated assets can be returned as hosted URLs or saved to a local path when requested.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
