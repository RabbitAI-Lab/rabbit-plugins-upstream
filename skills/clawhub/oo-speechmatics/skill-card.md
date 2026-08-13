## Description:

Speechmatics (speechmatics.com). Use this skill for Speechmatics requests involving reading, creating, and updating data through the OOMOL CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Speechmatics capabilities, submit Batch transcription jobs from media URLs, and retrieve job status, errors, and completed transcripts through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit Speechmatics Batch transcription jobs, which may consume account resources or process unintended media.

Mitigation: Confirm the exact payload and effect with the user before running the write action.

Risk: First-time setup includes a fallback CLI install command that runs a remote installer script.

Mitigation: Use the fallback installer only when the oo CLI is missing and review the install path before approving execution.

Risk: Incorrect transcription payloads or stale connector assumptions could produce failed jobs or misleading results.

Mitigation: Fetch the live connector schema before constructing payloads and review the returned job status, metadata, errors, and transcript format.

## Reference(s):

- [ClawHub Speechmatics skill page](https://clawhub.ai/oomol/skills/oo-speechmatics)
- [Speechmatics homepage](https://www.speechmatics.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Text, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses from the oo CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId; transcripts may be returned as JSON, plain text, or SRT.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
