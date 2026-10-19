## Description:

Helps agents generate videos from prompts and optional image, video, audio, or frame references through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct video generation with text prompts, multimedia references, and optional first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to the hosted dLazy service.

Mitigation: Only submit prompts and media that you intend to share with dLazy.

Risk: The dLazy API key is a credential saved locally by the CLI.

Mitigation: Protect the key and rotate or revoke it if exposed.

Risk: Using the external CLI may install a global package.

Mitigation: Use the documented pinned npx invocation if a global installation is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing generated-asset URLs or an asynchronous task ID.]

## Skill Version(s):

1.2.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
