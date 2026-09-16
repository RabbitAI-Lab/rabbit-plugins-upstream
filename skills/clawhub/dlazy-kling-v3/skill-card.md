## Description:

Powerful video generation with Kling v3, supporting high-quality text-to-video and image-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to invoke the dLazy Kling V3 video generation CLI for text-to-video and image-to-video workflows. The skill can return generated media URLs or asynchronous task identifiers and can save generated assets when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill executes an external npm CLI under the user's account.

Mitigation: Prefer one-time npx execution or a sandbox, and review the package before global installation.

Risk: Prompts and selected local media are sent to dLazy-hosted services.

Mitigation: Avoid uploading sensitive prompts or media unless that data is approved for dLazy processing.

Risk: The dLazy API key may be stored persistently in the local user configuration.

Mitigation: Use per-invocation credentials when practical and rotate or revoke the API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated media URLs, asynchronous task identifiers, and saved local asset paths through the dLazy CLI.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
