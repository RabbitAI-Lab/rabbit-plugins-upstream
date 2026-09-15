## Description:

ElevenReader lets agents use an OOMOL-connected ElevenLabs account to inspect text-to-speech models and voices, read text aloud, and retrieve user or subscription information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate ElevenReader through the OOMOL connector for voice discovery, text-to-speech generation, and account status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented fallback setup includes unverified remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use an official versioned installer with checksum or signature verification, avoid elevated shells unless required, and do not run pipe-to-shell or Invoke-Expression installers blindly.

Risk: Text submitted for speech generation is sent through OOMOL's connector to ElevenReader or ElevenLabs services.

Mitigation: Install and use the skill only when the user accepts OOMOL as the connector and is comfortable sending the submitted text for speech generation.

## Reference(s):

- [ElevenReader skill page](https://clawhub.ai/oomol/skills/oo-elevenreader)
- [ElevenReader homepage](https://elevenlabs.io/text-reader)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses that include generated audio references and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
