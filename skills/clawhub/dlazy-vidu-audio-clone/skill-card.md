## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Vidu Audio Clone workflow, providing a prompt and optional reference audio to generate cloned-voice speech output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and selected local audio or media files to dLazy hosted services.

Mitigation: Install only if you trust dLazy, avoid uploading voice samples without appropriate rights, and use the documented API key controls to rotate or revoke access.

Risk: The skill depends on a pinned third-party CLI that may be installed globally.

Mitigation: Prefer the documented npx invocation or a scoped local install, and review the @dlazy/cli package or source before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing result outputs or an asynchronous task identifier.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
