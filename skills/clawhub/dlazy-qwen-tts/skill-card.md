## Description:

Alibaba Bailian qwen3-tts text-to-speech generates spoken audio from text with curated system voices, dialect options, or a custom voice described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent invoke the dLazy Qwen TTS CLI for cloud text-to-speech generation, choose voices or describe a custom voice, and optionally save the returned generated asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the dLazy CLI globally creates a persistent third-party binary on the user's system.

Mitigation: Review the @dlazy/cli source before installation, or use the pinned npx invocation for on-demand execution.

Risk: The dLazy API key is a credential stored in local CLI configuration or supplied through an environment variable.

Mitigation: Treat the key as a secret, restrict local access, and rotate or revoke it from the dLazy dashboard if exposure is suspected.

Risk: Prompts, parameters, and referenced media files are sent to dLazy hosted API and media endpoints.

Mitigation: Use the skill only with content that is appropriate to send to the dLazy service and avoid submitting sensitive local files unintentionally.

Risk: The --save option writes generated assets to a local path and could overwrite important files if used carelessly.

Mitigation: Use --save only with an intentional output path and review the target location before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with bash command examples and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers; saved outputs can be written to a user-specified path.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
