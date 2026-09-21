## Description:

Voicemaker lets agents operate Voicemaker text-to-speech through an OOMOL-connected account, including generating speech audio and listing voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Voicemaker text-to-speech audio and browse available voices through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of a remote installer.

Mitigation: Review the oo CLI installer source and prefer a verified or package-manager installation path before use.

Risk: Voicemaker text-to-speech generation is a write action that may affect billing or credits.

Mitigation: Approve generation only after checking the exact text, voice, and expected billing impact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-voicemaker)
- [Voicemaker homepage](https://voicemaker.in/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector actions return JSON with generated audio URLs or voice lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI and an OOMOL-connected Voicemaker account; text-to-speech generation can affect billing or credits.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
