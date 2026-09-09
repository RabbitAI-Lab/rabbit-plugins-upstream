## Description:

Alibaba Bailian qwen3-tts text-to-speech that lets agents choose curated system voices, including dialects, or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Qwen TTS workflow from an agent, generating speech from text with either predefined voices or a described custom voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external dLazy npm CLI and relies on hosted dLazy services for text-to-speech generation.

Mitigation: Review the linked CLI source and npm package before installation; use the pinned npx invocation when a persistent global install is not desired.

Risk: Prompts, selected parameters, and local files explicitly passed to the CLI may be sent to dLazy API and storage endpoints.

Mitigation: Avoid submitting sensitive content unless approved for the dLazy service, and review inputs before execution.

Risk: A dLazy API key is stored locally or provided through the environment for authenticated use.

Mitigation: Keep the API key scoped and revocable, rotate it when needed, and avoid exposing it in logs or shared shell history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Guidance]

**Output Format:** [CLI command guidance plus JSON result envelopes containing generated asset URLs, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and access to dLazy API and file-hosting endpoints.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
