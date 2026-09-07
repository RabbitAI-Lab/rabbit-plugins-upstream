## Description:

Moonshot AI thinking model with text, image, and video understanding. Suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call dLazy's Kimi K3 command for complex analysis, coding, and writing from prompts with optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a pinned third-party dLazy CLI package and hosted API service.

Mitigation: Decide whether you trust the dLazy CLI package and service before installation; use npx or another isolated execution method if you do not want a global binary.

Risk: Prompts, parameters, and selected local files may be sent to dLazy API and media storage endpoints.

Mitigation: Provide only files intended for upload, protect the dLazy API key, and rotate or revoke the key if use stops or compromise is suspected.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [JSON response containing model outputs, or an async task identifier when --no-wait is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated output URLs hosted by dLazy media storage; --save can download returned assets.]

## Skill Version(s):

1.2.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
