## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample to clone a custom voice usable in later text-to-speech calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Qwen audio clone workflow from an agent, supplying an authorized clean voice sample and metadata to create a reusable custom voice for later TTS use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review marked the release suspicious because the documentation does not match the advertised command and the pinned CLI's live registry did not list that command during review.

Mitigation: Confirm dLazy currently supports `qwen-audio-clone` in the installed CLI before use; stop if help output or registry contents differ from the card.

Risk: Voice-cloning inputs may include biometric or personal audio data, and the skill sends selected audio and parameters to dLazy cloud services.

Mitigation: Only upload voice samples the user has rights and consent to use, and review dLazy service terms and data handling before submitting audio.

Risk: Authentication stores a dLazy API key locally.

Mitigation: Use `dlazy login` or `dlazy auth set` only on trusted machines, keep config permissions restricted to the OS user, and rotate or revoke keys from the dLazy dashboard if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, dLazy authentication, and a user-provided audio URL or local audio path.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
