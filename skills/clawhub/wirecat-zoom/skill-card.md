## Description:

Archive Zoom cloud recordings, read stored meeting transcripts and summaries, or manage a Zoom meeting through zm. Use for Zoom CLI workflows, not joining calls or operating the desktop video client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Zoom users and agents use this skill to search and read stored meeting evidence, archive recordings, and prepare or manage Zoom meetings through the zm CLI. It guides profile selection, source coverage checks, and review of commands that can change remote meeting state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanners report a benign result with medium confidence, but could not inspect some referenced material.

Mitigation: Review the referenced material and the Node package installation source before installing.

Risk: Some CLI commands can create, update, or cancel remote Zoom meetings.

Mitigation: Review the selected profile and proposed change, use a dry run when available, and inspect remote state before retrying an uncertain write.

## Reference(s):

- [Zoom Cli release on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-zoom)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text, JSON]

**Output Format:** [Markdown guidance with shell commands and structured JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results can include bounded meeting, transcript, archive, and coverage data.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
