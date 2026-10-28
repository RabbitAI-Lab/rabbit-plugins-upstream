## Description:

Moonshot AI thinking model with text, image, and video understanding. Suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can send prompts, images, and videos to Moonshot AI's Kimi K3 model for complex analysis, coding, and writing, then receive model output through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy-hosted services for processing.

Mitigation: Send only content you are authorized to share and comfortable submitting to the service.

Risk: The CLI saves a reusable API key locally, and requests may consume paid credits.

Mitigation: Protect the local configuration, review cost estimates before sending requests, and rotate or revoke the key when it is no longer needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy service](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Code]

**Output Format:** [JSON response envelope containing model-generated content; the content format depends on the prompt.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts text prompts and optional images or videos; asynchronous requests can return a task identifier.]

## Skill Version(s):

1.2.30 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
