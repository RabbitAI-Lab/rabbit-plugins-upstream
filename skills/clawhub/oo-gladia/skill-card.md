## Description:

Gladia helps agents manage Gladia pre-recorded transcription workflows through the OOMOL oo CLI, including listing, starting, retrieving, downloading, uploading, and deleting transcription jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users use this skill to operate Gladia transcription jobs through an OOMOL-connected account without handling raw API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback first-time setup asks users to run remote installer scripts directly in a shell.

Mitigation: Prefer an official package manager or manually download and verify the installer before running first-time setup commands.

Risk: The skill can start uploads or transcription jobs and can delete transcription data.

Mitigation: Review exact payloads before approval, and require explicit confirmation for write and destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gladia)
- [Gladia homepage](https://app.gladia.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON action responses and file references when upload or download actions run.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
