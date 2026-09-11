## Description:

PixVerse C1 helps agents generate videos from text, images, first and last frames, or reference images through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to invoke PixVerse C1 for text-to-video, image-to-video, first/last-frame video, and reference-image video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs an external dLazy npm CLI and sends prompts, selected media files, and the dLazy API key to the dLazy hosted service.

Mitigation: Review the linked source and npm package before use, prefer npx or an isolated environment when avoiding a global binary, and use only approved prompts and media files.

Risk: A saved dLazy API key may remain in local CLI configuration after authentication.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke the API key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as hosted result URLs, with optional local downloads through the CLI save flag.]

## Skill Version(s):

1.2.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
