## Description:

Moonshot AI thinking model with text, image, and video understanding. Suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send prompts to Kimi K3 for complex analysis, coding, and writing, with optional image and video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's cloud service, and local media may be uploaded for model processing.

Mitigation: Share only intended files and review the service's privacy terms before sending prompts or media.

Risk: Generation calls can consume paid credits.

Mitigation: Use the dry-run option to inspect the payload and cost estimate before making a call.

Risk: Saving an API key in the local CLI configuration stores a credential on the device.

Mitigation: Use the DLAZY_API_KEY environment-variable option if you prefer not to save the key locally, and keep credentials private.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)

## Skill Output:

**Output Type(s):** [Text, JSON, Media URLs]

**Output Format:** [JSON response envelope containing generated result content or media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-driven; optional image and video inputs; asynchronous task mode is available.]

## Skill Version(s):

1.2.28 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
