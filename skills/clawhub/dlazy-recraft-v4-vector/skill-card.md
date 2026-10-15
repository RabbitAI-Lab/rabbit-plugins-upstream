## Description:

Helps agents generate logo, icon, and other design assets from text prompts through dLazy's Recraft V4 Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and other users can ask an agent to create logo or icon assets from a text prompt and chosen aspect ratio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly referenced local media are sent to dLazy's hosted service, which requires an API key.

Mitigation: Use only content approved for upload, protect the API key, and rotate or revoke it if exposed.

Risk: The skill promises SVG output, but its example response identifies a PNG file.

Mitigation: Check the returned file type and verify that it is a true vector asset before using it for scalable designs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and a JSON response example]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may be available by hosted URL or saved locally; verify the actual file format before relying on vector scaling.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
