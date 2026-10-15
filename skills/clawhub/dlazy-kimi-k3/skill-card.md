## Description:

Uses Kimi K3 through dLazy to help with complex analysis, coding, and writing using text, image, or video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask Kimi K3 to analyze text and selected images or videos, draft writing, and assist with code through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service.

Mitigation: Use the service only when sharing those inputs with dLazy is acceptable; review selected files before uploading.

Risk: The dLazy CLI stores an API key in local configuration.

Mitigation: Protect the key as a credential and rotate or revoke it through the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [JSON response containing model-generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier instead of an immediate result.]

## Skill Version(s):

1.2.24 (source: ClawHub release metadata; bundled CLI instructions specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
