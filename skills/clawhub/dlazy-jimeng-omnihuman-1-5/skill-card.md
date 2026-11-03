## Description:

Generates digital human broadcast videos with Jimeng OmniHuman 1.5 from a portrait image and audio or text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create digital human broadcast videos from a portrait and audio or text using Jimeng OmniHuman 1.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portraits, audio, and prompts are sent to dLazy services, and media files may be uploaded for processing; hosted data retention is unverified.

Mitigation: Use the service only for media and prompts you are comfortable sharing with dLazy, and confirm consent and usage rights for the people and recordings involved.

Risk: CLI behavior and generation charges may not be fully understood before a request is submitted.

Mitigation: Review the CLI implementation if needed, use its dry-run option to inspect the payload and cost estimate, and check generation costs before submitting.

Risk: Sharing an API key in a conversation can expose account access.

Mitigation: Prefer the device-code login flow; keep credentials in the local CLI configuration or use the environment variable as documented.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website (listed in skill documentation)](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset and JSON result envelope with hosted output URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before the generated asset is ready.]

## Skill Version(s):

1.3.36 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
