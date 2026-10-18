## Description:

Advertised for Grok 4.2 text generation and chat, but the supplied instructions instead direct the agent to generate Midjourney-style images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking text generation, question answering, or chat may discover this release, but its supplied instructions lead to image generation instead. Confirm the intended task before using the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic chat triggers and the text-versus-image mismatch may cause unintended paid image-generation requests.

Mitigation: Confirm the intended task and command before invoking the service; preview cost where supported.

Risk: Prompts and selected local file paths may be sent to dLazy's cloud service.

Mitigation: Avoid sharing sensitive prompts or files and review the dLazy CLI package before installation.

Risk: The CLI can store an API key locally and paid credits may be consumed.

Mitigation: Use a revocable API key and check credit usage before making requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Image links]

**Output Format:** [JSON result containing an image URL, relayed as agent-facing text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests may return a task ID instead of an image link; errors may report missing credentials or insufficient credits.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
