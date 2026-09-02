## Description:

Generates realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to invoke dLazy's hosted Jimeng OmniHuman 1.5 service from an agent workflow, supplying a portrait plus audio or text and receiving generated video output links or saved assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image or audio files are sent to dLazy's hosted service for generation.

Mitigation: Use only media and prompts that are appropriate to share with the dLazy service, and review the service terms before handling sensitive content.

Risk: Invocations can consume account credits.

Mitigation: Use the documented --dry-run option for cost checks before submitting a generation request.

Risk: The skill installs or runs a third-party CLI package.

Mitigation: Use the pinned @dlazy/cli version declared by the skill and review the CLI package source when supply-chain assurance is required.

Risk: The skill should not be invoked unintentionally during general discussion of digital humans.

Mitigation: Invoke the dLazy command only when the user intends to generate a video.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs, async task identifiers, or saved local files when --save is used.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
