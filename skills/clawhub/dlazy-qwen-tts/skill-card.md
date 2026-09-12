## Description:

Alibaba Bailian qwen3-tts text-to-speech; agents can choose curated system voices, including dialects, or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's Qwen TTS workflow from an agent, producing speech audio from prompts with either predefined voices or natural-language voice design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and selected local media inputs to the dLazy cloud service for processing.

Mitigation: Only submit prompts and files that are acceptable to share with the service, and avoid sensitive or regulated content unless your organization has approved that use.

Risk: The skill depends on a third-party CLI and hosted endpoints outside NVIDIA's control.

Mitigation: Use the pinned CLI version, prefer npx for one-off execution when possible, and review the dLazy CLI source or package before installation in high-assurance environments.

Risk: A saved dLazy API key could be misused if exposed from the local environment.

Mitigation: Use a revocable API key, store it only through the CLI or environment variable mechanisms, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON response examples; generated assets are returned as hosted file URLs or saved local files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
