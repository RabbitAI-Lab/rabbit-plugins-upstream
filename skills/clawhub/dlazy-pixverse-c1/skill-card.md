## Description:

Helps agents generate PixVerse C1 videos from text, images, reference images, or first and last frames through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short PixVerse C1 videos from prompts and optional images, then retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to a third-party hosted service.

Mitigation: Confirm what will be shared before submitting sensitive content.

Risk: Video generation may consume paid credits.

Mitigation: Confirm before generation and use a cost estimate when appropriate.

Risk: The dLazy API key is stored locally when using CLI login.

Mitigation: Protect the key and revoke or rotate it when access is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include a hosted media link or an asynchronous task ID; local download is optional.]

## Skill Version(s):

1.2.33 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
