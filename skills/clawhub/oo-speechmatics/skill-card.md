## Description:

Speechmatics (speechmatics.com). Use this skill for Speechmatics requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Speechmatics through OOMOL's oo CLI, including capability checks, Batch job submission, status retrieval, and transcript download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can direct users to execute a remote installer script in a shell.

Mitigation: Install the oo CLI only from trusted channels; prefer manually downloading and verifying the installer before connecting Speechmatics.

Risk: The submit_transcription action creates a Speechmatics Batch job from a media URL.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Speechmatics skill page](https://clawhub.ai/oomol/skills/oo-speechmatics)
- [Speechmatics homepage](https://www.speechmatics.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Speechmatics connection](https://console.oomol.com/app-connections?provider=speechmatics)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Text, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing actions require user confirmation before execution; credentials are handled by the connected OOMOL account.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
