## Description:

Alibaba Bailian qwen3-tts voice cloning uploads a clean voice sample to clone a custom voice usable in subsequent text-to-speech calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Qwen Audio Clone workflow, upload authorized voice samples, and create custom voices for later text-to-speech generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive voice samples and uploads local audio to dLazy cloud services.

Mitigation: Only upload voice samples the user is authorized to clone, treat uploaded audio as sensitive, and confirm dLazy's retention and deletion terms before use.

Risk: The security verdict is suspicious and the evidence recommends reviewing package provenance before installation.

Mitigation: Review the dLazy CLI source and npm package provenance before use, prefer npx or another ephemeral setup, and use a limited or revocable API key.

Risk: Command documentation is contradictory for the voice-cloning parameters.

Mitigation: Run dlazy qwen-audio-clone -h or use dry-run mode to verify required parameters and payloads before submitting voice data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI metadata homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
