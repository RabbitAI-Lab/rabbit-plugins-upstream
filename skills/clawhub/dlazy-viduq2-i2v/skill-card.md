## Description:

Convert static images into dynamic videos using Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Vidu Q2 image-to-video service from an agent workflow, supplying prompts, reference images, frame images, audio options, duration, aspect ratio, and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy cloud endpoints for processing.

Mitigation: Use the skill only with content suitable for dLazy processing and avoid sending sensitive media unless that transfer is acceptable.

Risk: API keys can persist in the local dLazy CLI configuration.

Mitigation: Prefer DLAZY_API_KEY for per-run credentials on shared systems, or rotate and revoke saved keys from the dLazy dashboard when needed.

Risk: Global CLI installation persists a local executable.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when less local persistence is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return generated media URLs, asynchronous task IDs, or save generated assets to a local path.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
