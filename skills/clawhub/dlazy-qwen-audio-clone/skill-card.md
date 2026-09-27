## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample through the dLazy CLI to create a custom voice for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's hosted Qwen audio-cloning service from an agent workflow, supplying an audio sample, name, and description to create a reusable voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples, prompts, and related files are sent to dLazy's hosted service and may be stored or processed outside the local environment.

Mitigation: Use the skill only with audio and prompts that are approved for dLazy processing, and review dLazy service terms before use.

Risk: The skill stores a dLazy API key in local CLI configuration or accepts it through an environment variable.

Mitigation: Protect the local configuration file, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The artifact documentation contains mismatched examples and an incorrect-looking sample output for an audio-cloning command.

Mitigation: Verify current behavior with `dlazy qwen-audio-clone -h` and use `--dry-run` before sending sensitive or costly requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous generateId for polling.]

## Skill Version(s):

1.3.19 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
