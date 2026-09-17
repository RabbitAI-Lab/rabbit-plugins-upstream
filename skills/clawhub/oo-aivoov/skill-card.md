## Description:

AiVOOV helps an agent operate AiVOOV through an OOMOL-connected account to list voices and generate text-to-speech audio with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run AiVOOV text-to-speech workflows from an agent through an OOMOL-connected account. It supports listing available voices and generating base64 audio from one or more voice/text segments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code if followed without review.

Mitigation: Review and verify the OOMOL installer source before running it, or prefer a pinned, signed, or package-manager installation path.

Risk: The create_audio action is a write operation that can generate billable or persistent output from user-provided text and voice settings.

Mitigation: Confirm the exact text, voice, and expected output effects with the user before running create_audio.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aivoov)
- [AiVOOV homepage](https://aivoov.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, Code]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; create_audio returns base64 audio data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
