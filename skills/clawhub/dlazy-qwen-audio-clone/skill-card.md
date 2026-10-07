## Description:

Guides agents in cloning an authorized voice sample for use in subsequent Qwen3-TTS speech generation through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to submit voice samples they have permission to clone and obtain custom voices for later text-to-speech tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are uploaded to a hosted service without clear biometric-consent or retention guidance.

Mitigation: Clone only voices with explicit permission; avoid confidential or third-party recordings unless authorized, and check the provider's data practices before upload.

Risk: The dLazy CLI stores an API key locally and sends samples to the provider.

Mitigation: Install only if you trust dLazy with voice samples and key storage; protect and rotate the key when needed.

Risk: Published command examples and output descriptions are inconsistent.

Mitigation: Check the installed CLI's actual help and responses before integrating it into automated workflows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON results]

**Output Format:** [Markdown instructions with CLI commands and example JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included examples conflict with the listed CLI options and voice-cloning purpose; confirm actual CLI help and responses before automation.]

## Skill Version(s):

1.3.24 (source: ClawHub release; included skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
