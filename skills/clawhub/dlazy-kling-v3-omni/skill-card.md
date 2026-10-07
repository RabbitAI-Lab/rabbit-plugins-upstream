## Description:

Guides agents in generating Kling V3 Omni videos from text prompts and optional image or video references using the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short generated videos from text and optional reference media, then retrieve the resulting media links or files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the external dLazy CLI requires trusting its package before installation.

Mitigation: Review the package before use; choose the pinned on-demand npx invocation if a persistent global installation is not desired.

Risk: Prompts and explicitly supplied media are sent to dLazy's hosted service, and a saved API key persists in local configuration.

Mitigation: Only submit media you are comfortable sharing with dLazy; pass DLAZY_API_KEY per invocation if you do not want the CLI to save the key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands; the CLI returns JSON containing generated-media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs and optional download of generated media.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; included skill files list 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
