## Description:

This skill invokes dLazy's Seedance 2.0 video generation CLI to create videos from prompts and optional image, video, audio, or first/last-frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request Seedance 2.0 video generation through the dLazy CLI, including text-to-video, multimodal reference generation, and first/last-frame workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-provided image, video, or audio files are sent to dLazy hosted services for generation.

Mitigation: Do not submit sensitive media unless the user accepts dLazy processing; review dLazy service terms and use only approved inputs.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials or rotate/revoke keys from the dLazy dashboard when needed.

Risk: The skill installs or invokes an external npm CLI.

Mitigation: Prefer the pinned npx command for temporary use, and review the package or source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or async task IDs; --save can download generated assets.]

## Skill Version(s):

1.3.15 (source: server-resolved release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
