## Description:

Generates videos with Kling v3 Omni from prompts and optional image, video, or subject references through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to ask an agent to configure and run Kling v3 Omni video generation through the pinned dLazy CLI. It supports text-to-video and image/video-guided generation workflows that return generated media URLs or asynchronous task identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image, video, or audio paths are sent to dLazy services for generation.

Mitigation: Avoid sending sensitive or restricted media and review user-provided inputs before invoking the CLI.

Risk: The dLazy API key may be stored in the local CLI configuration or supplied through an environment variable.

Mitigation: Use user-scoped credentials, rotate or revoke keys when no longer needed, and avoid exposing keys in prompts, logs, or shared terminals.

Risk: Installing the pinned external CLI globally persists a third-party executable on the system.

Mitigation: Review the pinned @dlazy/cli package/source before installation or use the npx invocation to avoid a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated results are returned as hosted media URLs, or as an asynchronous generation ID when no-wait mode is used.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
