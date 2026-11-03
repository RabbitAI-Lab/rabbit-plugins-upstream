## Description:

Anthropic's latest Sonnet — near-Opus quality on coding and long-horizon agentic work at Sonnet cost, with support for reasoning, code generation, complex tool orchestration, and text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can send prompts to Claude Sonnet 5 through dLazy for text and code generation, reasoning, and complex tool-oriented tasks. They can include images or videos as input and save generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill's third-party CLI runs publisher-provided code.

Mitigation: Review the dLazy CLI project before installing, as the skill documentation recommends.

Risk: Prompts and uploaded media are sent to dLazy; uploaded media receives public URLs according to the publisher documentation cited in the security review.

Mitigation: Submit only content you intend to share with dLazy, and avoid sensitive prompts or media.

Risk: Login saves a dLazy API key in the local CLI configuration, and requests may consume dLazy credits.

Mitigation: Keep the local configuration private, rotate or revoke the key when needed, and use the CLI dry-run option to inspect a payload and cost estimate before calling the API.

## Reference(s):

- [CLI project page (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Files]

**Output Format:** [Model-generated content returned in a JSON response; generated assets can be saved as files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result format depends on the prompt; image and video inputs are supported.]

## Skill Version(s):

1.2.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
