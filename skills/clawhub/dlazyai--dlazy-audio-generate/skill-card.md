## Description:

Audio generation skill that selects an appropriate dLazy CLI audio or text-to-speech model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate speech, dialogue, music, and sound effects through dLazy-hosted audio models from natural-language prompts and supplied parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a pinned third-party npm CLI and sends audio prompts, parameters, and explicitly referenced media files to dLazy hosted services.

Mitigation: Install only after accepting the third-party CLI and cloud API data flow; use the pinned npx invocation when avoiding a persistent global install.

Risk: A dLazy API key is stored locally or supplied through the environment for authenticated requests.

Mitigation: Use the CLI authentication flow or environment variable deliberately, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked dLazy CLI returns JSON envelopes and hosted media URLs for generated audio outputs.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
