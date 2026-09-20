## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke the dLazy CLI for Google Veo 3.1 Fast video generation from prompts, frame images, or video-extension inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media can be sent to dLazy hosted services for generation.

Mitigation: Avoid passing private media unless upload to dLazy is intended, and review inputs before execution.

Risk: The skill depends on the third-party dLazy CLI and API key configuration.

Mitigation: Install only if the dLazy CLI is trusted, prefer the pinned npx command for non-persistent use, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: Cloud generation calls may consume account credits or fail because of authentication, balance, or service errors.

Mitigation: Use CLI help or dry-run behavior before paid calls and surface authorization or insufficient-balance errors clearly to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, async task identifiers, or downloaded local files when the CLI save option is used.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
