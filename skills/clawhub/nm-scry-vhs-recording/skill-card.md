## Description:

Generates terminal recordings using VHS tape scripts and produces GIF outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation authors use this skill to validate VHS tape files, run terminal recording workflows, and produce GIFs for CLI demos, tutorials, and documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tape files can run terminal commands during recording.

Mitigation: Inspect every typed, sourced, or executed command before running VHS.

Risk: Recordings may expose secrets or internal details, especially when published publicly.

Mitigation: Avoid recording secrets and use --publish only after confirming the recording is safe to share.

Risk: The workflow depends on local tools such as VHS, ttyd, and ffmpeg.

Mitigation: Verify required tools are installed and check generated GIF files before using them in documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-vhs-recording)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry)
- [VHS Execution Guide](artifact/modules/execution.md)
- [VHS Tape Syntax Reference](artifact/modules/tape-syntax.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands and VHS tape snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions for creating or verifying GIF outputs from VHS tape files.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
