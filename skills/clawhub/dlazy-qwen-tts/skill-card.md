## Description:

Provides Alibaba Bailian qwen3-tts text-to-speech through the dLazy CLI, using curated system voices or custom voices designed from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate speech from text with Alibaba Bailian qwen3-tts through the dLazy hosted API, selecting a system voice or describing a custom voice. It is suited for agent workflows that can invoke the pinned dLazy CLI and send prompts to a cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supported local files supplied to the CLI are processed by dLazy's hosted service.

Mitigation: Only send data that is appropriate for third-party cloud processing, and review the dLazy service and CLI source before use in sensitive environments.

Risk: The dLazy API key can be stored locally and reused by the CLI.

Mitigation: Protect the local CLI configuration, prefer per-invocation environment credentials where operationally appropriate, and rotate or revoke keys that are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API Calls, Text, Markdown, Guidance]

**Output Format:** [JSON response with generated media URLs or async task status, plus concise Markdown guidance for setup and recoverable errors.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and supported input files are processed by dLazy's hosted service and generated outputs are returned as hosted URLs.]

## Skill Version(s):

1.3.8 (source: evidence.release.version; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
