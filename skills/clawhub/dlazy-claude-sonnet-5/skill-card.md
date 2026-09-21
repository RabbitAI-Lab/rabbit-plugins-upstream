## Description:

Anthropic's latest Sonnet -- near-Opus quality on coding and long-horizon agentic work at Sonnet cost, with support for text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to call dLazy's Claude Sonnet 5 wrapper for text generation, coding, reasoning, and multimodal prompt workflows through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This skill depends on a third-party dLazy CLI and account service.

Mitigation: Before installing or invoking it, confirm that you trust the dLazy CLI and service account used for generation.

Risk: dLazy API keys are required and may be stored in the local dLazy CLI configuration or supplied through an environment variable.

Mitigation: Use OS user file permissions for local configuration, avoid exposing the key in shared shells, and rotate or revoke the key when it is no longer needed.

Risk: Local files passed as image, video, or audio inputs may be uploaded to dLazy media storage.

Mitigation: Do not pass sensitive local files unless upload to dLazy is intended and acceptable for the user or organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON responses from the dLazy CLI, with generated content returned in output values or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input plus optional image and video inputs; local media paths may be uploaded through the dLazy CLI when supplied.]

## Skill Version(s):

1.2.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
