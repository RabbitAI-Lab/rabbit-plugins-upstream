## Description:

AiVOOV helps agents operate AiVOOV through an OOMOL-connected account to create audio and list available voices with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run AiVOOV text-to-speech workflows through an OOMOL-connected account, including creating base64 audio and listing voices by optional language code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes one-line remote installer commands for the oo CLI without verification.

Mitigation: Use a verified, version-pinned oo CLI installation method with signatures or checksums before running AiVOOV actions.

Risk: The create_audio action can change AiVOOV state or consume account resources.

Mitigation: Confirm the exact payload and intended effect with the user before executing write actions.

## Reference(s):

- [ClawHub AiVOOV Skill](https://clawhub.ai/oomol/skills/oo-aivoov)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [AiVOOV Homepage](https://aivoov.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return command output containing AiVOOV action data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
