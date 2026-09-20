## Description:

SunoAPI (sunoapi.org). Use this skill for reading, creating, updating, and deleting SunoAPI data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate SunoAPI through OOMOL-connected credentials, including music generation, audio extension, covers, mashups, lyrics, MIDI, video, WAV conversion, vocal separation, and account credit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run remote installer scripts without verification.

Mitigation: Review the OOMOL oo CLI installation path before installing and prefer a verified package, signed release, or manually downloaded installer with checksum or signature validation.

Risk: Write or destructive SunoAPI actions can change account data or consume credits.

Mitigation: Confirm the exact payload and effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub SunoAPI Skill Page](https://clawhub.ai/oomol/skills/oo-sunoapi)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [SunoAPI Homepage](https://sunoapi.org)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit SunoAPI actions through the oo CLI and return task identifiers, generated content details, account credit information, or setup guidance.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
