## Description:

Speechmatics (speechmatics.com). Use this skill for Speechmatics requests involving reading, creating, and updating data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Speechmatics connector schemas, query Speechmatics capabilities and deployments, submit Batch transcription jobs, and retrieve job status or transcripts through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Use a verified, pinned, or package-manager installation path where possible and avoid running pasted installer commands blindly.

Risk: Speechmatics requests are mediated through OOMOL.

Mitigation: Install only when use of OOMOL as an intermediary is acceptable for the deployment.

Risk: The skill can submit Batch transcription jobs that change state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-speechmatics)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Speechmatics Homepage](https://www.speechmatics.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Speechmatics connector responses as JSON, plain text transcripts, or SRT subtitles depending on the selected action.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
