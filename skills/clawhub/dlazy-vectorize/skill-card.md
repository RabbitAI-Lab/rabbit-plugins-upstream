## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to convert bitmap images such as logos, icons, and flat illustrations into scalable vector output through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, prompts, and parameters are sent to the dLazy hosted API and media storage.

Mitigation: Install and use the skill only when comfortable sending those inputs to dLazy; avoid submitting sensitive images unless approved for that workflow.

Risk: The skill depends on the third-party dLazy CLI and ordinary npm dependency trust.

Mitigation: Prefer the pinned npx or local install path when possible, and review the linked package and source before installing globally.

Risk: A saved dLazy API key can be misused if exposed from the local configuration or environment.

Mitigation: Keep the key scoped to the operating-system user, use environment variables only for the current invocation when appropriate, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI can return a hosted result URL, and asynchronous runs may return a generateId for polling.]

## Skill Version(s):

1.2.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
