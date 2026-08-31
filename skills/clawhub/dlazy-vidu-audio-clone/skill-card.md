## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Vidu Audio Clone workflow for generating speech in a cloned voice from text and optional reference audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload reference audio and prompts to dLazy-hosted services.

Mitigation: Use it only with audio and text the user owns or has explicit permission to process, and tell users to expect prompts and media files to be uploaded to dLazy.

Risk: Voice cloning can generate impersonation-capable speech without clear consent guardrails in the artifact.

Mitigation: Require explicit permission for the voice being cloned and avoid generating speech that impersonates a person without consent.

Risk: The workflow depends on a dLazy API key and may incur account charges.

Mitigation: Prefer dry-run or npx until the workflow is trusted, keep the API key revocable, and confirm the command is available in the CLI environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through dLazy-hosted output URLs; asynchronous calls can return a generation ID for later polling.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
