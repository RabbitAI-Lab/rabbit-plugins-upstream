## Description:

Guides agents in generating videos with Seedance 2.5 through dLazy using text prompts, reference media, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from prompts and optional image, video, audio, or frame references through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media are sent to the hosted dLazy service.

Mitigation: Only submit prompts and media you intend to share with dLazy.

Risk: Authentication can save a dLazy API key in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: Using the skill installs or runs a third-party npm CLI.

Mitigation: Review the package before running it; use the pinned npx invocation to avoid a global install.

## Reference(s):

- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and shell commands; CLI results are JSON with generated asset URLs or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may be saved locally with the CLI's --save option.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata; skill text lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
