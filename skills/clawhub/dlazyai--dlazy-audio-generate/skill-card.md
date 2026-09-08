## Description:

Selects an appropriate dLazy audio model for text-to-speech, dialogue, music, voice search, and sound-effect generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route audio-generation requests to the appropriate dLazy CLI model for TTS, multi-speaker dialogue, music, sound effects, or voice discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media paths may be sent to dLazy infrastructure for generation.

Mitigation: Avoid sensitive prompts or files and use the skill only when cloud processing by dLazy is acceptable.

Risk: The skill installs or runs a third-party CLI package.

Mitigation: Review the pinned npm package and source before global installation, or use the pinned npx command for on-demand execution.

Risk: Authentication can save an API key in a local user configuration file.

Mitigation: Prefer DLAZY_API_KEY in shared or one-off environments and rotate or revoke organization keys when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated audio results are returned by the dLazy CLI as JSON URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy hosted APIs and may reference output files hosted by dLazy.]

## Skill Version(s):

1.3.16 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
